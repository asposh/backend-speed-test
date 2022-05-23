import multiprocessing
import re
from .cmd import CMD
from .config import Config


class Monitoring:
    """
    BST resources monitoring
    """

    def __init__(self, config: Config) -> None:
        """ Initialise monitoring """

        self.config = config
        self.process = None
        self.resources = multiprocessing.Manager().dict({
            "memory_max": 0
        })

    def get_resources(self) -> dict:
        """ Get resources """

        resources = dict(self.resources)
        return resources

    def start(self, obj_type: str, obj_name: str) -> None:
        """
        Start solutuon or storage monitoring
        obj_type = "solutions" or "storages"
        """

        container = (
            self.config.params["settings"]["container-prefix"]
            + self.config.params[obj_type][obj_name]["container"]
        )
        self.process = multiprocessing.Process(
            target=Monitoring.check_max_resources,
            args=(container, self.resources)
        )
        self.process.start()

    def stop(self):
        """ Stop solutuon or storage monitoring """

        self.process.terminate()

    def check_max_resources(container: str, resources: dict) -> None:
        """ Check maximum container resources (memory) """

        stats = CMD.docker_stats(container)
        for line in iter(stats.stdout.readline, b''):
            memory = Monitoring.__parse_usage_mem(line)
            resources["memory_max"] = max(resources["memory_max"], memory)

    def __parse_usage_mem(parse_line: str) -> float:
        """ Parse usage memory from string """

        string = Monitoring.__remove_ansi_escape(parse_line.decode('utf-8'))
        for i in range(len(string)):
            if string[i].isalpha():
                memory = float(string[0:i])
                if (string[i].lower() == "g"):
                    memory *= 1024
                return memory

    def __remove_ansi_escape(string: str) -> str:
        """ Remove ANSI escape sequences from string"""

        ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]")
        result = ansi_escape.sub("", string)
        return result
