from utils.Trees.Tree import Tree
from utils.Trees.Treap import Treap
from utils.Trees.ScapegoatTree import ScapegoatTree
from utils.Trees.SplayTree import SplayTree
from utils.Tests import test_generator, test_handler
from utils.Tests.test_generator import TestConfig
from time import time
from typing import List


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        tree = func(*args, **kwargs)
        end = time()

        return tree, round(end - start, 2)

    return wrapper

@timer
def generateTree(tree: Tree, arr: List[int]):
    for elem in arr:
        tree.insert(elem)
    return tree

def main():
    test_generator.generate_test("Treaps_test", [
        TestConfig(1_000_000, 10_000_000)
    ])
    treap_path = "tests/random_generated/Treaps_test"
    for test in test_handler.read_file(treap_path):
        #The number of priority possibilites = 10 * max_val
        treap = Treap(0, 10 * test.length)
        treap, duration = generateTree(treap, test.array)

        try:
            test_handler.verify_Treap(treap, test.length)
            print("Treap generation duration:", duration, 'sec')
        except AssertionError as error:
            print(f"Treap generation failed: {str(error)}")


if __name__ == "__main__":
    main()