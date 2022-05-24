import argparse
import os
import shutil
import requests
from .helper import Helper
from ..bst import BST
from ..config import Config
from ..docker import Docker
from ..jmeter import Jmeter
from ..logger import Logger
from ..monitoring import Monitoring
from ..report import Report


class TestBST():
    """
    Test BST
    """

    def setup_method(self):
        self.config = Config(Helper.params,  Logger())
        self.test_case = "test_case_1"

    def test_run(self, mocker) -> None:
        """ Test: BST run """

        mocker.patch.object(Docker, '__init__', return_value=None)
        mocker.patch.object(Jmeter, '__init__', return_value=None)
        mocker.patch.object(BST, 'run_test_case')

        bst = BST(Helper.params)
        bst.run()
        BST.run_test_case.assert_called_once_with(self.test_case)

    def test_run_test_case_cli_arg(self, mocker) -> None:
        """ Test: BST run with "tase_case" cli argument """

        mocker.patch.object(Docker, '__init__', return_value=None)
        mocker.patch.object(Jmeter, '__init__', return_value=None)
        mocker.patch.object(BST, 'run_test_case')

        add_argument = mocker.Mock()
        args = argparse.Namespace()
        args.test_case = "test_case_2"
        parse_args = mocker.Mock(return_value=args)
        parser = mocker.Mock(add_argument=add_argument, parse_args=parse_args)
        mocker.patch.object(argparse, 'ArgumentParser', return_value=parser)

        bst = BST(Helper.params)
        bst.run()
        BST.run_test_case.assert_called_once_with(args.test_case)
        add_argument.assert_called_with("test_case", type=str, nargs='?', help=mocker.ANY)

    def test_run_test_case(self, mocker) -> None:
        """ Test: BST run test case """

        mocker.patch.object(Docker, '__init__', return_value=None)
        mocker.patch.object(Docker, 'container_start')
        mocker.patch.object(Docker, 'container_stop')

        mocker.patch.object(Monitoring, 'start')
        mocker.patch.object(Monitoring, 'stop')
        resources = mocker.Mock()
        mocker.patch.object(Monitoring, 'get_resources', return_value=resources)

        mocker.patch.object(Jmeter, '__init__', return_value=None)
        mocker.patch.object(Jmeter, 'run')

        report_test = mocker.Mock()
        mocker.patch.object(Report, 'solution', return_value=report_test)
        mocker.patch.object(Report, 'test_case')

        request_mock = mocker.Mock(status_code=200)
        mocker.patch.object(requests, 'get', return_value=request_mock)

        bst = BST(Helper.params)
        bst.run_test_case(self.test_case)

        testcase_dir = f"{self.config.params['bst_path']}/data/reports/{self.test_case}"
        for dir in os.listdir(testcase_dir):
            if dir.isnumeric():
                time_dir = dir
        report_dir = f"{testcase_dir}/{time_dir}"
        assert os.path.exists(report_dir)

        solutions_call = []
        storages_call = []
        report_solutions_dict = {}
        jmetr_call = []
        report_solutions_call = []
        request_calls = []
        test_settings = self.config.get_test_settings(self.test_case)
        if "storages" in self.config.params["test-plan"][self.test_case]:
            for storage in self.config.params["test-plan"][self.test_case]["storages"]:
                storages_call.append(
                    mocker.call(
                        "storages",
                        storage
                    )
                )
        for solution in self.config.params["test-plan"][self.test_case]["solutions"]:
            report_solutions_dict[solution] = report_test
            solutions_call.append(mocker.call("solutions", solution))
            report_solution_dir = f"{report_dir}/{solution}"
            report_solutions_call.append(
                mocker.call(
                    self.test_case,
                    test_settings,
                    solution,
                    report_solution_dir,
                    resources
                 )
            )
            jmetr_call.append(
                mocker.call(
                    self.test_case,
                    report_solution_dir
                )
            )
            request_calls.append(
                mocker.call(
                    self.config.params["test-plan"][self.test_case]["ready-check"],
                    verify=False
                )
            )

            assert os.path.exists(report_solution_dir)

            setup_dir = (
                f"{self.config.params['bst_path']}/data/reports/{self.test_case}/"
                f"test_setup/{solution}"
            )
            setup_before = f"{setup_dir}/before"
            setup_after = f"{setup_dir}/after"
            assert os.path.exists(setup_before)
            assert os.path.exists(setup_after)
        shutil.rmtree(testcase_dir)

        Docker.container_start.assert_has_calls(storages_call + solutions_call)
        Docker.container_stop.assert_has_calls(solutions_call + storages_call)

        Monitoring.start.assert_has_calls(solutions_call)
        assert len(Monitoring.stop.mock_calls) == len(solutions_call)
        assert len(Monitoring.get_resources.mock_calls) == len(solutions_call)

        Jmeter.run.assert_has_calls(jmetr_call)

        Report.solution.assert_has_calls(report_solutions_call)
        Report.test_case.assert_called_once_with(
            self.test_case,
            report_dir,
            report_solutions_dict,
            mocker.ANY
        )

        requests.get.assert_has_calls(request_calls)
