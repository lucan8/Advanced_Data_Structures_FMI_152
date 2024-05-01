from utils.Trees.Tree import Tree
from utils.Tests import test_handler
from time import time
from typing import List
def benchmark(func):
    def wrapper(*args, **kwargs):
        try:
            successful_operations, duration = func(*args, **kwargs)
            #args[0]-tree, args[1]-arr
            test_handler.verify_Treap(args[0], len(args[1]))

            print(func.__name__,
                  f"({len(args[1])} elements, {successful_operations} successful):", 
                  duration)
        except AssertionError as error:
            print(f"Failed at {func.__name__}: ", str(error))

    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        successful_operations = func(*args, **kwargs)
        end = time()
        return successful_operations, round(end - start, 2)

    wrapper.__name__ = func.__name__
    return wrapper

@benchmark
@timer
def blockInsert(tree: Tree, arr: List[int]) -> int:
    inserted = 0
    for elem in arr:
        inserted += tree.insert(elem)
    return inserted

@benchmark
@timer
def blockRemove(tree: Tree, arr: List[int]) -> int:
    removed = 0
    for elem in arr:
        removed += tree.remove(elem)
    return removed

@benchmark
@timer
def blockSearch(tree: Tree, arr: List[int]) -> int:
    found = 0
    for elem in arr:
        found += (tree.search(elem) is None)
    return found