import multiprocessing
from .helper import Helper
from ..config import Config
from ..cmd import CMD
from ..logger import Logger
from ..monitoring import Monitoring


class TestMonitoring():
    """
    Test Monitoring
    """

    def setup_method(self):
        self.config = Config(Helper.params,  Logger())
        self.container = (
            f"{self.config.params['settings']['container-prefix']}"
            "test_solution_container1"
        )
        self.resources = multiprocessing.Manager().dict({
            "memory_max": 0
        })

    def test_start(self, mocker):
        """ Test: start """

        monitoring = Monitoring(self.config)

        start = mocker.Mock()
        process = mocker.Mock(start=start)

        mocker.patch.object(
            multiprocessing,
            'Process',
            autospec=True,
            return_value=process
        )
        monitoring.start("solutions", "test_solution_1")
        multiprocessing.Process.assert_called_with(
            target=Monitoring.check_max_resources,
            args=(self.container, monitoring.resources)
        )
        start.assert_called()
        assert monitoring.process == process

    def test_stop(self, mocker):
        """ Test: stop """

        monitoring = Monitoring(self.config)
        terminate = mocker.Mock()
        process = mocker.Mock(terminate=terminate)

        monitoring.process = process
        monitoring.stop()
        terminate.assert_called()

    def test_get_resources(self):
        """ Test: Get resources """

        monitoring = Monitoring(self.config)
        monitoring.resources = self.resources
        monitoring.resources["memory_max"] = 10.1
        resources = monitoring.get_resources()
        test_resources = {
            "memory_max": 10.1
        }
        assert resources == test_resources

    def test_check_max_resources(self, mocker) -> None:
        """ Test: Check max resources """

        lines = [
            "11.1MiB / 11.11GiB".encode('ASCII'),
            "15.2MiB / 11.11GiB".encode('ASCII'),
            "10.11MiB / 11.11GiB".encode('ASCII'),
            "".encode('ASCII'),
        ]
        readline = mocker.Mock(side_effect=iter(lines))
        stdout = mocker.Mock(readline=readline)
        stats = mocker.Mock(stdout=stdout)

        mocker.patch.object(
            CMD,
            'docker_stats',
            autospec=True,
            return_value=stats
        )

        Monitoring.check_max_resources(self.container, self.resources)

        assert self.resources["memory_max"] == 15.2
