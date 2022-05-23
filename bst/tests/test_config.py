import os
from .helper import Helper
from ..logger import Logger
from ..config import Config


class TestConfig():
    """
    Test Config
    """

    def setup_method(self):
        self.logger = Logger()
        self.params = Helper.params
        self.config_path = f"{self.params['bst_path']}/config.yml"

    def test_load(self) -> None:
        """ Test: config load """

        config = Config(self.params, self.logger)

        assert os.path.exists(self.config_path)

        if os.path.exists(self.config_path):
            os.remove(self.config_path)

        test_params = {
            "bst_path": self.params["bst_path"],
            "settings": {
                "container-prefix": "test-",
                "jmetr-source": "test-jmeter.zip",
            },
            "storages": {
                "test_storage": {
                    "title": "Test title",
                    "container": "test_storage_container",
                    "start-delay": 2,
                },
            },
            "solutions": {
                "test_solution_1": {
                    "title": "Test solution 1",
                    "container": "test_solution_container1",
                },
                "test_solution_2": {
                    "title": "Test solution 2",
                    "container": "test_solution_container2",
                }
            },
            "test-plan": {
                "test_case_1": {
                    "title": "Title test-case",
                    "run": True,
                    "jmx": "environment/test-plan/test_case_1.jmx",
                    "setup": "environment/test-plan/setup/test_case_1.py",
                    "ready-check": "https://localhost",
                    "storages": [
                        "test_storage",
                    ],
                    "solutions": [
                        "test_solution_1",
                        "test_solution_2",
                    ],
                },
                "test_case_2": {
                    "title": "Title test-case 2 no run",
                    "run": False,
                    "jmx": "environment/test-plan/test_case_1.jmx",
                    "ready-check": "https://localhost",
                    "solutions": [
                        "test_solution_1",
                    ],
                },
            },
        }

        assert config.params == test_params

    def test_test_settings(self, capsys) -> None:
        """ Test: test settings """

        config = Config(self.params, self.logger)

        test_settings = {
            'loops': 5,
            'threads': 10,
            'ramp_time': 3,
            'on_error': 'stoptestnow',
            'stress_test': True
        }

        settings = config.get_test_settings("test_case_1")

        assert settings == test_settings
