import json
import os
import time
from .helper import Helper
from ..config import Config
from ..logger import Logger
from ..report import Report


class TestReport():
    """
    Test Report
    """

    def setup_method(self):
        self.logger = Logger()
        self.config = Config(Helper.params, self.logger)
        self.report = Report(self.config, self.logger)
        self.test_case = "test_case_1"

    def test_solution(self) -> None:
        """ Test: Solution report """

        test_settings = {
            'loops': 5,
            'threads': 10,
            'ramp_time': 3,
            'on_error': 'stoptestnow',
            'stress_test': True
        }
        solution = "test_solution_1"

        report_solution_dir = (
            f"{self.config.params['bst_path']}/data/reports/report_dir_test/solution_dir_test"
        )

        data = {
            "additional_data": "any"
        }

        report_dict = self.report.solution(
            self.test_case,
            test_settings,
            solution,
            report_solution_dir,
            data
        )

        check_dict = data | {
            'title': self.config.params["solutions"][solution]["title"],
            'time_start': 1651782424.696,
            'time_end': 1651782426.882,
            'time_duration': 2.186,
            'res_prc90th': 183.6,
            'res_min': 11.0,
            'res_max': 687.0,
            'errors': 0,
            'connections_max': 10
        }

        assert report_dict == check_dict

    def test_test_case(self, mocker) -> None:
        """ Test: Test-case report  """

        time_start = time.time()
        report_dir = f"{self.config.params['bst_path']}/data/reports/report_dir_test"
        report_file = f"{report_dir}/{self.test_case}_result.json"
        solution_report = {
            "test_solution_1": {
                "test_param_1": 10,
            },
            "test_solution_2": {
                "test_param_2": 20,
            }
        }
        report_dict = {
            "test-case": self.test_case,
            "title": self.config.params['test-plan'][self.test_case]['title'],
            "time_start": time_start,
            "solutions": solution_report
        }

        if os.path.exists(report_file):
            os.remove(report_file)

        self.report.test_case(self.test_case, report_dir, solution_report, time_start)

        with open(report_file) as json_file:
            data = json.load(json_file)

        assert data == report_dict
