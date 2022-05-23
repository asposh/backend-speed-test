import os
import shutil
import urllib.request
import zipfile
from .logger import Logger
from .config import Config
from .cmd import CMD


class Jmeter:
    """
    JMeter manager
    """

    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger
        self.__load()

    def run(self, test_case: str, report_solution_dir: str) -> None:
        """ Run JMeter test """

        test_case_jmx = self.config.params["test-plan"][test_case]["jmx"]

        self.logger.info("Run JMeter test")
        CMD.jmeter_run(self.config.params["bst_path"], test_case_jmx, report_solution_dir)

    def __load(self) -> None:
        """ Load JMeter """

        self.logger.info("Load JMeter")
        jmeter_path = f"{self.config.params['bst_path']}/environment/jmeter"

        if os.path.exists(f"{jmeter_path}/app/bin"):
            return

        self.__download(jmeter_path)
        self.__unzip(jmeter_path)
        temp_dir = self.__copy_to_app(jmeter_path)
        os.chmod(f"{jmeter_path}/app/bin/jmeter", 0o755)
        self.__delete_temp(jmeter_path, temp_dir)

    def __download(self, jmeter_path: str) -> None:
        """ Download JMeter """

        self.logger.info("Download JMeter")
        urllib.request.urlretrieve(
            self.config.params["settings"]["jmetr-source"],
            f"{jmeter_path}/jmeter.zip"
        )

    def __unzip(self, jmeter_path: str) -> None:
        """ JMeter unzip """

        self.logger.info("Unzip JMeter")
        with zipfile.ZipFile(f"{jmeter_path}/jmeter.zip", 'r') as zip:
            zip.extractall(f"{jmeter_path}/app")

    def __copy_to_app(self, jmeter_path: str) -> str:
        """ Copy JMeter files to app folder """

        self.logger.info("Copy JMeter files to app folder ")
        temp_dir = os.listdir(f"{jmeter_path}/app")[0]
        shutil.copytree(f"{jmeter_path}/app/{temp_dir}", f"{jmeter_path}/app", dirs_exist_ok=True)

        return temp_dir

    def __delete_temp(self, jmeter_path: str, temp_dir: str) -> None:
        """ Delete temp files """

        self.logger.info("Delete temporary JMeter files")
        shutil.rmtree(f"{jmeter_path}/app/{temp_dir}")
        os.remove(f"{jmeter_path}/jmeter.zip")
