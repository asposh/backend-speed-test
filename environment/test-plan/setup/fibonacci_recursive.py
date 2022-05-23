import os
import csv
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

        csv_dir = f"{self.bst.config.params['bst_path']}/environment/test-plan/csv"
        csv_path = f"{csv_dir}/fibonacci_recursive.csv"

        if os.path.exists(csv_path):
            return

        os.makedirs(csv_dir, exist_ok=True)

        data = []
        for i in range(20, 41):
            data.append([i])

        csv_file = open(csv_path, 'w')
        with csv_file:
            writer = csv.writer(csv_file, dialect='unix')
            writer.writerows(data)

    def after(self, solution: str = ""):
        """ After test """

        pass
