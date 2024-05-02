from typing import List
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


