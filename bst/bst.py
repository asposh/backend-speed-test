import argparse
import datetime
import importlib.util
import os
import requests
import time
import urllib3
from .config import Config
from .docker import Docker
from .jmeter import Jmeter
from .logger import Logger
from .monitoring import Monitoring
from .report import Report


class BST:
    """
    Backend speed test(BST)
    """

    def __init__(self, params: dict):
        """
        BST initialise
        """

        if not params or "bst_path" not in params:
            raise ValueError("params['bst_path'] is required")

        self.cli_args = self.__parse_cli_args()
        self.logger = Logger()
        self.config = Config(params, self.logger)
        self.jmeter = Jmeter(self.config, self.logger)
        self.docker = Docker(self.config, self.logger)
        self.report = Report(self.config, self.logger)

        # Disable InsecureRequestWarning for https requests
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def run(self) -> None:
        """ Run backend speed test """

        # Run special test case (forced)
        if self.cli_args.test_case:
            self.run_test_case(self.cli_args.test_case)
            return

        # Run test cases
        for test_case in self.config.params["test-plan"]:
            if ("run" in self.config.params["test-plan"][test_case]
                    and not self.config.params["test-plan"][test_case]["run"]):
                continue
            self.run_test_case(test_case)

    def run_test_case(self, test_case) -> None:
        """ Run test case """

        self.logger.info(f"Start test-case: {test_case}")

        time_start = time.time()
        time_dir = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        solutions_report = {}
        report_dir = f"{self.config.params['bst_path']}/data/reports/{test_case}/{time_dir}"
        test_settings = self.config.get_test_settings(test_case)
        test_setup = self.__setup_test(test_case)

        # Start storage containers
        self.__storages_containers(test_case, "start")

        for solution in self.config.params["test-plan"][test_case]["solutions"]:
            solutions_report[solution] = self.__run_solution(
                test_case,
                test_settings,
                test_setup,
                solution,
                report_dir
            )

        # Make test case report
        self.report.test_case(test_case, report_dir, solutions_report, time_start)

        # Stop storage containers
        self.__storages_containers(test_case, "stop")

        self.logger.info(f"Test-case: {test_case} complete")

    def __run_solution(
        self,
        test_case: str,
        test_settings: dict,
        test_setup: object,
        solution: str,
        report_dir: str
    ) -> dict:
        """ Run solution """

        self.logger.info(f"Start solution: {solution}")

        monitoring = Monitoring(self.config)
        report_solution_dir = f"{report_dir}/{solution}"

        # Make report directory
        os.makedirs(report_solution_dir, exist_ok=True)

        self.__start_solution_test(test_case, test_setup, solution, monitoring)
        self.jmeter.run(test_case, report_solution_dir)
        self.__stop_solution_test(test_case, test_setup, solution, monitoring)

        resources = monitoring.get_resources()
        report = self.report.solution(
            test_case,
            test_settings,
            solution,
            report_solution_dir,
            resources
        )

        self.logger.info(f"Solution: {solution} complete")

        return report

    def __start_solution_test(
        self,
        test_case: str,
        test_setup: str,
        solution: str,
        monitoring: Monitoring
    ) -> None:
        """ Start solution test """

        # Start solution container
        self.docker.container_start("solutions", solution)
        self.__wait(self.config.params["test-plan"][test_case]["ready-check"])

        # Setup before solution
        if test_setup:
            self.logger.info(f"Setup(before) test-case: {test_case}")
            test_setup.before(solution)

        # Start monitoring
        monitoring.start("solutions", solution)

    def __stop_solution_test(
        self,
        test_case: str,
        test_setup: str,
        solution: str,
        monitoring: Monitoring
    ) -> None:
        """ Stop solution test """

        # Stop monitoring
        monitoring.stop()

        # Setup after solution
        if test_setup:
            self.logger.info(f"Setup(after) test-case: {test_case}")
            test_setup.after(solution)

        # Stop solution container
        self.docker.container_stop("solutions", solution)

    def __storages_containers(self, test_case: str, action: str) -> None:
        """ Start/stop storage containers """

        if "storages" not in self.config.params["test-plan"][test_case]:
            return

        for storage in self.config.params["test-plan"][test_case]["storages"]:
            method = getattr(self.docker, f"container_{action}")
            method("storages", storage)

    def __setup_test(self, test_case: str) -> object:
        """ Test setup initialise """

        if 'setup' not in self.config.params['test-plan'][test_case]:
            return None

        setup_path = self.config.params['test-plan'][test_case]['setup']
        setup_path = f"{self.config.params['bst_path']}/{setup_path}"

        spec = importlib.util.spec_from_file_location(f"setup.{test_case}", setup_path)
        imported = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported)
        test_setup = imported.Setup(self, test_case)

        return test_setup

    def __wait(self, url: str) -> None:
        """ Waiting for solution readiness """

        self.logger.info("Waiting for solution readiness")
        while True:
            try:
                check = requests.get(url, verify=False)
                if check.status_code == 200:
                    return
            except Exception:
                pass

            time.sleep(1)

    def __parse_cli_args(self) -> argparse.Namespace:
        """ Parsing cli arguments """

        parser = argparse.ArgumentParser(description="Backend speed test (BST)")

        # Cli arguments
        parser.add_argument("test_case", type=str, nargs='?', help='Run special test-case (forced)')

        args = parser.parse_args()

        return args
