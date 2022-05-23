import os
import csv
import hashlib
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

        requests.get("https://localhost/entity/delete_all", verify=False)

        csv_dir = f"{self.bst.config.params['bst_path']}/environment/test-plan/csv"
        csv_path = f"{csv_dir}/add_entity.csv"
        if os.path.exists(csv_path):
            return

        os.makedirs(csv_dir, exist_ok=True)

        data = []
        for i in range(50000):
            row = [
                hashlib.md5(str(i).encode('utf-8')).hexdigest(),
                i,
            ]
            data.append(row)

        csv_file = open(csv_path, 'w')
        with csv_file:
            writer = csv.writer(csv_file, dialect='unix')
            writer.writerows(data)

    def after(self, solution: str = ""):
        """ After test """

        requests.get("https://localhost/entity/delete_all", verify=False)
