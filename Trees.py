from abc import abstractmethod
from random import randint
MAX_RANDOM = 5000000

class Node:
    def __init__(self, key : int, priority : int):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


class TreapNode(Node):
    def __init__(self, key : int, priority : int):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.father = None


class Tree:
    def __init__(self):
        self.root = None
    @abstractmethod
    def search(self, node : int) -> Node:
        ...

    @abstractmethod
    def insert(self, node : int) -> bool: #Returns true if insertion was done, false otherwise
        ...

    @abstractmethod
    def remove(self, node : int) -> bool: #Returns true if removal was done, false otherwise
        ...


class ScapegoatTree(Tree):
    def search(self, node : int):
        ...
    
    def insert(self, node : int):
        ...

    def remove(self, node : int):
        ...


class SplayTree(Tree):
    def search(self, node : int):
        ...
    
    def insert(self, node : int):
        ...

    def remove(self, node : int):
        ...

#Unique elements only
#Can two nodes have the same priority?
class Treap(Tree):
    def search(self, node : int) -> TreapNode:
        BST_iterator = self.root

        while (BST_iterator):
            if (node == BST_iterator.key):
                return BST_iterator
            elif node > BST_iterator.key:
                BST_iterator = BST_iterator.right
            else:
                BST_iterator = BST_iterator.left
        return None
    
    def insert(self, node : int) -> bool:
        global MAX_RANDOM

        if not self.root:
            self.root = TreapNode(node, randint(0, MAX_RANDOM))
            return True
        
        BST_iterator = self.root
        while (True):
            if node > BST_iterator.key: 
                if (not BST_iterator.right): #Inserting node at right of current node
                    BST_iterator.right = TreapNode(node, randint(0, MAX_RANDOM))
                    BST_iterator.right.father = BST_iterator.right
                    return True
                
                BST_iterator = BST_iterator.right #Going to the right subtree
            elif node < BST_iterator.key: 
                if (not BST_iterator.left): #Inserting node at left of curr node
                    BST_iterator.left = TreapNode(node, randint(0, MAX_RANDOM))
                    BST_iterator.left.father = BST_iterator.left
                    return True
                
                BST_iterator = BST_iterator.left #Going to the left subtree
            else: #No node gets inserted if it already exists
                return False
    
    def remove(self, node : int) -> bool:
        del_node = self.search(node)
        if (not del_node):
            return False
        
        if del_node < del_node.father: #Left node
            if del_node.left and del_node.right:
                new_del_node = self.getLeftMostNode(del_node.right)
                del_node.key = new_del_node.key
                del_node = new_del_node

            self.__removeLeft(del_node)
        else:
            if del_node.left and del_node.right: #Right node
                new_del_node = self.getRightMostNode(del_node.left)
                del_node.key = new_del_node.key
                del_node = new_del_node

            self.__removeRight(del_node)
    
    #Make removed nodes inaccesible(set father and son to none)
    #Treat cases when you don't actually have those lefts and rights
    def __removeLeft(self, node : TreapNode):
        if not node.right: 
            node.father.left = node.left
            node.left.father = node.father
        elif not node.left: 
            node.father.left = node.right
            node.right.father = node.father

    def __removeRight(self, node : TreapNode):
        if not node.right: 
            node.father.right = node.left
            node.left.father = node.father
        elif not node.left: 
            node.father.right = node.right
            node.right.father = node.father

    def getLeftMostNode(self, root : Node) -> Node:
        while (root.left):
            root = root.left
        return root
    def getRightMostNode(self, root : Node) -> Node:
        while (root.right):
            root = root.right
        return root
                    