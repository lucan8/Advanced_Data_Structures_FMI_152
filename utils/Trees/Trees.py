from abc import abstractmethod


class Node:
    def __init__(self, key: int, priority: int = 0):
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
