import csv
import json
import os
from .config import Config
from .logger import Logger


class Report:
    """
    BST Report
    """

    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger

    def test_case(
        self,
        test_case: str,
        report_dir: str,
        solutions_report: dict,
        time_start: float
    ) -> None:
        """ Build test-case report """

        report = {
            "test-case": test_case,
            "title": self.config.params['test-plan'][test_case]['title'],
            "time_start": time_start,
            "solutions": solutions_report,
        }
        self.__write_result(test_case, report_dir, report)

    def solution(
        self,
        test_case: str,
        test_settings: dict,
        solution: str,
        report_solution_dir: str,
        data: dict = {}
    ) -> dict:
        """ Build solution report """

        data["title"] = self.config.params["solutions"][solution]["title"]
        data |= self.__get_test_time(report_solution_dir)
        data |= self.__get_test_statistics(report_solution_dir)
        data["connections_max"] = test_settings["threads"]
        # Stress test
        if (
            test_settings["stress_test"]
            and test_settings["loops"] == test_settings["threads"]
            and "ramp_time" in test_settings
        ):
            data["connections_max"] = int(
                data["time_duration"] * (test_settings["threads"] / test_settings["ramp_time"])
            )

        return data

    def __write_result(
        self,
        test_case: str,
        report_dir: str,
        report: dict
    ) -> None:
        """ Write report """

        json_report = json.dumps(report, indent=2)

        with open(f"{report_dir}/{test_case}_result.json", 'w') as fp:
            fp.write(json_report)

        self.logger.info(f"{test_case} results: {report_dir}")

    def __get_test_statistics(self, report_solution_dir: str) -> dict:
        """ Get test statistics """

        report_stat_path = f"{report_solution_dir}/dashboard/statistics.json"
        if not os.path.exists(report_stat_path):
            return {}

        statistics = {}
        json_params = {
            "pct1ResTime": "res_prc90th",
            "minResTime": "res_min",
            "maxResTime": "res_max",
            "errorCount": "errors",
        }

        with open(report_stat_path) as json_file:
            data = json.load(json_file)
            key = "Total"
            for param in json_params:
                if param in data[key]:
                    statistics[json_params[param]] = data[key][param]

        return statistics

    def __get_test_time(self, report_solution_dir: str) -> dict:
        """ Get test time """

        test_time = {}

        with open(
            f"{report_solution_dir}/request_log.csv",
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as csvdata:
            lines = list(csv.reader(csvdata))
            if len(lines) < 3:
                raise AssertionError("Test is too short")

            test_time["time_start"] = int(lines[1][0]) / 1000
            test_time["time_end"] = int(lines[-1][0]) / 1000
            test_time["time_duration"] = round(
                test_time["time_end"] - test_time["time_start"],
                3
            )

        return test_time
