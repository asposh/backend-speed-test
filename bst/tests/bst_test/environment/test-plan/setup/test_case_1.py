import os
from bst import bst


class Setup:
    """
    Setup "test" test-plan
    """

    def __init__(self, bst_instance: bst.BST, test_case: str = ""):
        self.bst = bst_instance
        self.test_case = test_case

    def before(self, solution: str = ""):
        """ Before test """

        test_path = (
            f"{self.bst.config.params['bst_path']}/data/reports/"
            f"{self.test_case}/test_setup/{solution}/before"
        )
        os.makedirs(test_path, exist_ok=True)

    def after(self, solution: str = ""):
        """ After test """

        test_path = (
            f"{self.bst.config.params['bst_path']}/data/reports/"
            f"{self.test_case}/test_setup/{solution}/after"
        )
        os.makedirs(test_path, exist_ok=True)
