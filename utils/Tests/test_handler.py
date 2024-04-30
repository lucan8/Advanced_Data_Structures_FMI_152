from typing import List
from utils.Trees.Treap import Treap
from queue import Queue
class TestUnit:
    def __init__(self, index: int, array: List[int], length: int, max_value: int):
        self.index = index
        self.array = array
        self.length = length
        self.max_value = max_value


def read_file(path):
    final_tests: List[TestUnit] = []

    with open(path, "r") as input_file:
        nr_of_tests = int(input_file.readline())

        for test_index in range(nr_of_tests):
            array_length, max_value = [
                int(num) for num in input_file.readline().split()]
            array = [int(num) for num in input_file.readline().split()]

            final_tests.append(
                TestUnit(test_index + 1, array, array_length, max_value))

    return final_tests

def verify_Treap(treap : Treap, size: int):
    assert __isTreap__(treap) is True, "Treap properties violated!"

def __isTreap__(treap : Treap) -> bool:
    if not treap.root:
        return True
    
    q = Queue()
    q.put(treap.root)

    while not q.empty():
        elem = q.get()

        if elem.left:
            if elem.left.key >= elem.key or elem.left.priority > elem.priority:
                return False
            
            q.put(elem.left)
        
        if elem.right:
            if elem.right.key <= elem.key or elem.right.priority > elem.priority:
                return False
            
            q.put(elem.right)

    return True


