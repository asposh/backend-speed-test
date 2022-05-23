import os
import sys

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
from bst.bst import BST  # noqa: E402


def main():
    """ Run speed test """

    bst = BST({
        "bst_path": path,
    })
    bst.run()


if __name__ == '__main__':
    main()
