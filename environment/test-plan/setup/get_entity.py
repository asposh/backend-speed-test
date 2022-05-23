import requests
from bst import bst


class Setup:
    """
    Setup get entity
    """

    def __init__(self, bst_instance: bst.BST, test_case: str = ""):
        self.bst = bst_instance
        self.test_case = test_case

    def before(self, solution: str = ""):
        """ Before test """

        data = {
            "name": "c4ca4238a0b923820dcc509a6f75849b"
        }
        requests.get("https://localhost/entity/delete_all", verify=False)
        requests.post("https://localhost/entity/", data=data, verify=False)

    def after(self, solution: str = ""):
        """ After test """

        requests.get("https://localhost/entity/delete_all", verify=False)
