import subprocess


class CMD:
    """
    Cli commands
    """

    def docker_stats(container: str) -> subprocess.Popen:
        """ Check docker stats (memory) """
        process = subprocess.Popen(
            "docker stats --format \"{{ .MemUsage }}\" " + container,
            stdout=subprocess.PIPE,
            shell=True
        )
        return process

    def docker_container_start(container: str) -> None:
        """ Start docker container """

        subprocess.call([
            "docker",
            "start",
            container,
        ])

    def docker_container_stop(container: str) -> None:
        """ Stop docker container """

        subprocess.call([
            "docker",
            "stop",
            container,
        ])

    def docker_composer_up(bst_path: str) -> None:
        """ Build docker containers """

        subprocess.call([
            "docker-compose",
            "up",
            "--no-start",
        ], cwd=bst_path)

    def jmeter_run(bst_path: str, test_case_jmx: str, report_solution_dir: str) -> None:
        """ JMeter test run """

        subprocess.call(" ".join([
                f"{bst_path}/environment/jmeter/app/bin/jmeter",
                "-e",
                "-f",
                "-n",
                "-i",
                f"{bst_path}/environment/jmeter/log4j2.xml",
                "-l",
                f"{report_solution_dir}/request_log.csv",
                "-o",
                f"{report_solution_dir}/dashboard",
                "-t",
                f"{bst_path}/{test_case_jmx}",
            ]),
            shell=True,
            cwd=bst_path
        )
