import time
from .logger import Logger
from .cmd import CMD
from .config import Config


class Docker:
    """
    Docker container manager
    """

    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger
        self.__docker_up()

    def container_start(self, obj_type: str, obj_name: str) -> None:
        """
        Start solutuon or storage container
        obj_type = "solutions" or "storages"
        """

        self.logger.info(f"Start {obj_type} container: {obj_name}")
        CMD.docker_container_start(
            self.config.params["settings"]["container-prefix"]
            + self.config.params[obj_type][obj_name]["container"]
        )

        if "start-delay" in self.config.params[obj_type][obj_name]:
            self.__container_start_delay(self.config.params[obj_type][obj_name]["start-delay"])

    def container_stop(self, obj_type: str, obj_name: str) -> None:
        """
        Stop solutuon or storage container
        obj_type = "solutions" or "storages"
        """

        self.logger.info(f"Stop {obj_type} container: {obj_name}")
        CMD.docker_container_stop(
            self.config.params["settings"]["container-prefix"]
            + self.config.params[obj_type][obj_name]["container"]
        )

    def __container_start_delay(self, sec: int) -> None:
        """ Delay after containers start """

        self.logger.info(f"Waiting: {sec} seconds")
        time.sleep(sec)

    def __docker_up(self):
        """ Docker containers initialise """

        self.logger.info("Docker containers initialise")
        CMD.docker_composer_up(self.config.params["bst_path"])
