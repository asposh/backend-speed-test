import subprocess
from .helper import Helper
from ..cmd import CMD
from ..config import Config
from ..logger import Logger


class TestCMD():
    """
    Test CMD
    """

    def setup_method(self):
        self.config = Config(Helper.params, Logger())
        self.container = "test_solution_container1"

    def test_docker_stats(self, mocker) -> None:
        """ Test: Docker stats """

        mocker.patch.object(subprocess, "Popen", return_value=1)
        process = CMD.docker_stats(self.container)

        test_command = "docker stats --format \"{{ .MemUsage }}\" " + self.container
        subprocess.Popen.assert_called_with(test_command, stdout=subprocess.PIPE, shell=True)
        assert process == 1

    def test_docker_start(self, mocker) -> None:
        """ Test: Docker start """

        mocker.patch.object(subprocess, "call")
        CMD.docker_container_start(self.container)

        test_command = [
            "docker",
            "start",
            self.container,
        ]
        subprocess.call.assert_called_with(test_command)

    def test_docker_stop(self, mocker) -> None:
        """ Test: Docker stop """

        mocker.patch.object(subprocess, "call")
        CMD.docker_container_stop(self.container)

        test_command = [
            "docker",
            "stop",
            self.container,
        ]
        subprocess.call.assert_called_with(test_command)

    def test_docker_composer_up(self, mocker) -> None:
        """ Test: Docker composer up """

        mocker.patch.object(subprocess, "call")
        CMD.docker_composer_up(self.config.params["bst_path"])

        test_command = [
            "docker-compose",
            "up",
            "--no-start",
        ]
        subprocess.call.assert_called_with(
            test_command,
            cwd=self.config.params["bst_path"]
        )

    def test_jmeter_run(self, mocker) -> None:
        """ Test: JMeter test run """

        mocker.patch.object(subprocess, "call")

        test_case_jmx = self.config.params["test-plan"]["test_case_1"]["jmx"]
        report_solution_dir = "test_dir"
        CMD.jmeter_run(self.config.params["bst_path"], test_case_jmx, report_solution_dir)

        test_command = " ".join([
            f"{self.config.params['bst_path']}/environment/jmeter/app/bin/jmeter",
            "-e",
            "-f",
            "-n",
            "-i",
            f"{self.config.params['bst_path']}/environment/jmeter/log4j2.xml",
            "-l",
            f"{report_solution_dir}/request_log.csv",
            "-o",
            f"{report_solution_dir}/dashboard",
            "-t",
            f"{self.config.params['bst_path']}/{test_case_jmx}",
        ])

        subprocess.call.assert_called_with(
            test_command,
            shell=True,
            cwd=self.config.params["bst_path"]
        )
