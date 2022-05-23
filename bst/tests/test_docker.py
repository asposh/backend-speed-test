import time
from .helper import Helper
from ..docker import Docker
from ..cmd import CMD
from ..config import Config
from ..logger import Logger


class TestDocker():
    """
    Test Docker
    """

    def setup_method(self):
        self.logger = Logger()
        self.config = Config(Helper.params, self.logger)

    def test_docker_up(self, mocker) -> None:
        """ Test: Docker up """

        self.__get_docker(mocker)
        CMD.docker_composer_up.assert_called_with(self.config.params["bst_path"])

    def test_container_start(self, mocker) -> None:
        """ Test: Docker container start """

        docker = self.__get_docker(mocker)
        mocker.patch.object(CMD, 'docker_container_start')
        solution = "test_solution_1"
        docker.container_start("solutions", solution)
        CMD.docker_container_start.assert_called_with(
            self.config.params["settings"]["container-prefix"]
            + self.config.params["solutions"][solution]["container"]
        )

        mocker.patch.object(time, 'sleep')
        storage = "test_storage"
        docker.container_start("storages", storage)
        CMD.docker_container_start.assert_called_with(
            self.config.params["settings"]["container-prefix"]
            + self.config.params["storages"][storage]["container"]
        )
        time.sleep.assert_called_with(self.config.params["storages"][storage]["start-delay"])

    def __get_docker(self, mocker):
        """ Get docker instance """

        mocker.patch.object(CMD, 'docker_composer_up')
        docker = Docker(self.config, self.logger)
        return docker
