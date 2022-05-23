import os
import shutil
import urllib.request
from .helper import Helper
from ..cmd import CMD
from ..config import Config
from ..jmeter import Jmeter
from ..logger import Logger


class TestJmeter():
    """
    Test JMeter
    """

    def setup_method(self):
        self.logger = Logger()
        self.config = Config(Helper.params, self.logger)

    def test_load(self, mocker) -> None:
        """ Test: JMeter load """

        jmeter_path = f"{self.config.params['bst_path']}/environment/jmeter/app"
        if os.path.exists(jmeter_path):
            shutil.rmtree(jmeter_path)

        def copy_zip(*args, **kwargs):
            shutil.copyfile(f"{self.config.params['bst_path']}/{args[0]}", args[1])

        mocker.patch.object(
            urllib.request,
            'urlretrieve',
            side_effect=copy_zip
        )
        mocker.patch.object(os, 'chmod')

        Jmeter(self.config, self.logger)
        os.chmod.assert_called_with(
            f"{self.config.params['bst_path']}/environment/jmeter/app/bin/jmeter",
            0o755
        )
        assert os.path.exists(f"{jmeter_path}/bin")

    def test_run(self, mocker) -> None:
        """ Test: JMeter run """

        jmeter = Jmeter(self.config, self.logger)
        mocker.patch.object(CMD, 'jmeter_run')
        test_case = "test_case_1"
        test_case_jmx = self.config.params["test-plan"][test_case]["jmx"]
        report_solution_dir = f"{self.config.params['bst_path']}/data/report/test_dir"
        jmeter.run(test_case, report_solution_dir)

        CMD.jmeter_run.assert_called_with(
            self.config.params['bst_path'],
            test_case_jmx,
            report_solution_dir
        )
