from abc import abstractmethod
from random import randint
from enum import Enum
from typing import List, Tuple

class RANDOM_LIMTIS(Enum):
    MAX_RANDOM = 5000000
    MIN_RANDOM = 0

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
class Treap1(Tree):
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
    #Bubble up the priority
    def insert(self, node : int) -> bool:
        new_node = TreapNode(node, randint(RANDOM_LIMTIS.MIN_RANDOM, RANDOM_LIMTIS.MAX_RANDOM))

        if not self.root:
            self.root = new_node
            return True
        
        BST_iterator = self.root
        while (True):
            if node > BST_iterator.key: 
                if (not BST_iterator.right): #Inserting node at right of current node
                    BST_iterator.right = new_node
                    BST_iterator.right.father = BST_iterator

                    self.__bubblePriority(BST_iterator.right)
                    return True
                
                BST_iterator = BST_iterator.right #Going to the right subtree
            elif node < BST_iterator.key: 
                if (not BST_iterator.left): #Inserting node at left of curr node
                    BST_iterator.left = new_node
                    BST_iterator.left.father = BST_iterator

                    self.__bubblePriority(BST_iterator.left)
                    return True
                
                BST_iterator = BST_iterator.left #Going to the left subtree
            else: #No node gets inserted if it already exists
                return False
    
    def remove(self, node : int) -> bool:
        del_node = self.search(node)
        #Node not found
        if (not del_node):
            return False
        
        if not del_node.father or del_node.key < del_node.father.key: #Left node
            if del_node.left and del_node.right:
                new_del_node = self.getLeftMostNode(del_node.right) #Getting smallest node in right subtree
                del_node.key = new_del_node.key 
                del_node = new_del_node 

            self.__removeLeft(del_node)
        else:
            if del_node.left and del_node.right: #Right node
                new_del_node = self.getRightMostNode(del_node.left) #Getting biggest node in left subtree
                del_node.key = new_del_node.key
                del_node = new_del_node

            self.__removeRight(del_node)
        return True
    
    def __removeLeft(self, node : TreapNode):
        #Leaf
        if not node.right and not node.left:
            node.father.left = None
        #No right subtree
        elif not node.right: 
            node.father.left = node.left
            node.left.father = node.father
            node.left = None
        #No left subtree
        elif not node.left: 
            node.father.left = node.right
            node.right.father = node.father
            node.right = None

        node.father = None

    def __removeRight(self, node : TreapNode):
        #Leaf
        if not node.right and not node.left:
            node.father.right = None
        #No right subtree
        elif not node.right: 
            node.father.right = node.left
            node.left.father = node.father
            node.left = None
        #No left subtree
        elif not node.left: 
            node.father.right = node.right
            node.right.father = node.father
            node.right = None

        node.father = None


    def getLeftMostNode(self, root : Node) -> Node:
        while (root.left):
            root = root.left
        return root
    def getRightMostNode(self, root : Node) -> Node:
        while (root.right):
            root = root.right
        return root

    def __bubblePriority(self, node : TreapNode):
        Treap_iterator = node
        while (Treap_iterator.father and Treap_iterator.father.priority < Treap_iterator.priority):
            node.father.priority, node.priority = node.priority, node.father.priority
            Treap_iterator = Treap_iterator.father

#Unique elements only
class Treap2:
    def __init__(self, root : Node = None) -> None:
        self.root = root

    def search(self, node : int) -> Node:
        Treap_iterator = self.root

        while (Treap_iterator):
            if (node == Treap_iterator.key):
                return Treap_iterator
            elif node > Treap_iterator.key:
                Treap_iterator = Treap_iterator.right
            else:
                Treap_iterator = Treap_iterator.left
        return None
    
    #Make a search fo this as well
    def insert(self, node : int) -> bool:
        new_node = Node(node, randint(RANDOM_LIMTIS.MIN_RANDOM, RANDOM_LIMTIS.MAX_RANDOM))

        if not self.root: #If there is no root we create it
            self.root = new_node
            return True
        
        Treap_iterator = self.root
        parent_stack = [] #Keeping all possible parents of the inserted node
        while (True):
            parent_stack.append(Treap_iterator)

            if node > Treap_iterator.key: 
                if (not Treap_iterator.right): #Inserting node at right of current node
                    Treap_iterator.right = new_node
                    self.__bubbleUpPriority(parent_stack, new_node)
                    return True
                
                Treap_iterator = Treap_iterator.right #Going to the right subtree
            elif node < Treap_iterator.key: 
                if (not Treap_iterator.left): #Inserting node at left of curr node
                    Treap_iterator.left = new_node
                    self.__bubbleUpPriority(parent_stack, new_node)
                    return True
                
                Treap_iterator = Treap_iterator.left #Going to the left subtree
            else: #No node gets inserted if it already exists
                return False
    
    #Verify bubble down priority
    def remove(self, node : int) -> bool:
        parent_del_node, del_node = self.__findRemoveNode(node)

        if not del_node: #Node not found so we don't delete
            return False

        del_node.priority = RANDOM_LIMTIS.MIN_RANDOM - 1

        #Getting the parent of the node after it's been bubbled down
        parent_del_node = self.__bubbleDownPriority(parent_del_node, del_node)
        
        #Deleting the node
        if not parent_del_node: #Removing the root as the only node
            self.root = None
        elif parent_del_node.left and parent_del_node.left.key == del_node.key:
            parent_del_node.left = None
        elif parent_del_node.right.key == del_node.key:
            parent_del_node.right = None

        return True

    
    #Returns the node to be deleted and it's parent
    def __findRemoveNode(self, node : int) -> Tuple[Node, Node]:
        Treap_iterator = self.root

        while (Treap_iterator):
            if node > Treap_iterator.key: #Verifying if the node is in right subtree
                if (Treap_iterator.right and Treap_iterator.right.key == node):
                    return Treap_iterator, Treap_iterator.right
                
                Treap_iterator = Treap_iterator.right #Going to the right subtree
            elif node < Treap_iterator.key: #Verifying if the node is in the left subtree
                if (Treap_iterator.left and Treap_iterator.left.key == node):
                    return Treap_iterator, Treap_iterator.left
                
                Treap_iterator = Treap_iterator.left #Going to the left subtree
            else:
                 return None, Treap_iterator #Root
            
        return None, None #Node not found

    def __bubbleUpPriority(self, parent_stack : List[Node], new_node : Node):
        while parent_stack:
            parent = parent_stack.pop()

            if parent_stack:
                grandparent = parent_stack[-1]
            else:
                grandparent = None

            #If the heap property is met then we stop
            if parent.priority >= new_node.priority:
                return

            if parent.right and parent.right.key == new_node.key: #Right child implies left rotation
                self.__leftRotation(grandparent, parent)

            elif parent.left and parent.left.key == new_node.key: #Left child implies right rotation
                self.__rightRotation(grandparent, parent)

    #Makes rotations in order to get the node to be a leaf and returns it's parent
    def __bubbleDownPriority(self, parent : Node, del_node : Node) -> Node:
        while (del_node.left or del_node.right):
            if not del_node.left:
                parent = self.__leftRotation(parent, del_node)
            elif not del_node.right:
                parent = self.__rightRotation(parent, del_node)
            elif del_node.right.priority > del_node.left.priority:
                parent = self.__leftRotation(parent, del_node)
            else:
                parent = self.__rightRotation(parent, del_node)

        return parent
            
    #Maybe remove the ifs and connect the old_father in each function
    def __rightRotation(self, father_old_root : Node, old_root : Node) -> Node:
        new_root = old_root.left
        new_root_right = new_root.right

        new_root.right = old_root
        old_root.left = new_root_right

        if father_old_root:
            if new_root.key > father_old_root.key:
                father_old_root.right = new_root
            else:
                father_old_root.left = new_root
        else: #No parent implies it has become the root
            self.root = new_root

        return new_root

    #Maybe remove the ifs and connect the old_father in each function
    def __leftRotation(self, father_old_root : Node, old_root : Node) -> Node:
        new_root = old_root.right
        new_root_left = new_root.left

        new_root.left = old_root
        old_root.right = new_root_left

        if father_old_root:
            if new_root.key > father_old_root.key:
                father_old_root.right = new_root
            else:
                father_old_root.left = new_root
        else: #No parent implies it has become the root
            self.root = new_root

        return new_root