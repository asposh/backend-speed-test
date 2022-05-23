import os
import shutil
import yaml
from xml.etree import ElementTree
from .logger import Logger


class Config:
    """
    BST config
    """

    def __init__(self, params: dict, logger: Logger):
        self.params = params
        self.logger = logger
        self.config_path = f"{self.params['bst_path']}/config.yml"
        self.template_path = f"{self.params['bst_path']}/environment/bst/template.config.yml"
        self.__load()

    def get_test_settings(self, test_case: str) -> dict:
        """ Get test plan settings """

        settings = {}

        test_case_jmx = self.params["test-plan"][test_case]["jmx"]
        root = ElementTree.parse(f"{self.params['bst_path']}/{test_case_jmx}").getroot()

        params = {
            "loops": {
                "name": "LoopController.loops",
                "type": "int"
            },
            "threads": {
                "name": "ThreadGroup.num_threads",
                "type": "int"
            },
            "ramp_time": {
                "name": "ThreadGroup.ramp_time",
                "type": "int"
            },
            "on_error": {
                "name": "ThreadGroup.on_sample_error",
                "type": "str"
            },
        }

        for param in params:
            value = root.find(f".//*[@name='{params[param]['name']}']").text
            if value is None:
                continue
            if params[param]['type'] == "int":
                settings[param] = int(value)
                continue
            settings[param] = value

        settings["stress_test"] = False
        if settings["on_error"] == "stoptestnow" or settings["on_error"] == "stoptest":
            settings["stress_test"] = True

        return settings

    def __load(self) -> None:
        """ Load config """

        self.logger.info("Load config")

        if not os.path.exists(self.config_path):
            self.logger.info("Initialise new config.yml file")
            shutil.copyfile(self.template_path, self.config_path)

        self.params = self.__parse_config() | self.params

    def __parse_config(self) -> None:
        """ Parse sonfig file """

        with open(self.config_path, "r") as content:
            try:
                return yaml.safe_load(content)
            except yaml.YAMLError as exc:
                raise SystemError(f"Can't load config data {exc}")
