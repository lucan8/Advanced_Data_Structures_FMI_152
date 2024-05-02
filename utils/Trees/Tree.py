from abc import abstractmethod
from typing import List
from time import time

def benchmark(func):
    def wrapper(*args, **kwargs):
            successful_operations, duration = func(*args, **kwargs)
            #args[0]-tree, args[1]-arr
            if (not args[0].meetsRequirments()):
                print(f"Failed at {func.__name__}: {args[0].__class__.__name__} requirments violated!")
            else:
                print(func.__name__,
                    f"({len(args[1])} elements, {successful_operations} successful):", 
                    duration)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        succsessful_operations = func(*args, **kwargs)
        end = time()

        return succsessful_operations, round(end - start, 2)

    wrapper.__name__ = func.__name__
    return wrapper

class Node:
    def __init__(self, key : int, priority : int = 0):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Returns the node with key = node(arg)
    @abstractmethod
    def search(self, node: int) -> Node:
        ...

    # Returns true if insertion was done, false otherwise
    @abstractmethod
    def insert(self, node: int) -> bool:
        ...

    # Returns true if removal was done, false otherwise
    @abstractmethod
    def remove(self, node: int) -> bool:
        ...
    #Meets requirements for said data structure
    @abstractmethod
    def meetsRequirments(self) -> bool:
        ...
    
    @benchmark
    @timer
    def blockSearch(self, arr: List[int]) -> int:
        found = 0
        for elem in arr:
            found += (self.search(elem) is not None)
        return found

    @benchmark
    @timer
    def blockInsert(self, arr: List[int]) -> int:
        inserted = 0
        for elem in arr:
            inserted += self.insert(elem)
        return inserted

    @benchmark
    @timer
    def blockRemove(self, arr: List[int]) -> int:
        removed = 0
        for elem in arr:
            removed += self.remove(elem)
        return removed
