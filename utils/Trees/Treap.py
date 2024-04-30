from Trees import Tree, Node
from random import randint
from enum import IntEnum
from typing import List, Tuple

#Maybe ask for these arguments in the constrcutor of the treap
#The nr of possible priorities shall be larger than the number of nodes
class RANDOM_LIMTIS(IntEnum):
    MAX_RANDOM : int = 5000000
    MIN_RANDOM : int = 0

#Unique elements only
class Treap(Tree):
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
    
    def insert(self, node : int) -> bool:
        ascendents_stack, new_node = self.__BSTInsert(node)

        if not new_node:
            return False
        
        self.__bubbleUpPriority(ascendents_stack, new_node)
        return True
    
    def remove(self, node : int) -> bool:
        parent_del_node, del_node = self.__findRemoveNode(node)

        if not del_node: #Node not found so we don't delete
            return False

        del_node.priority = RANDOM_LIMTIS.MIN_RANDOM - 1

        #Getting the parent of the node after it's been bubbled down
        parent_del_node = self.__bubbleDownPriority(parent_del_node, del_node)

        self.__removeLeaf(parent_del_node, del_node)

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
    
    #Returns a stack of all ascendents, and the node that was inserted
    def __BSTInsert(self, node : int) -> Tuple[List[Node], Node]:
        new_node = Node(node, randint(int(RANDOM_LIMTIS.MIN_RANDOM), int(RANDOM_LIMTIS.MAX_RANDOM)))

        if not self.root: #If there is no root we create it
            self.root = new_node
            return None, new_node
        
        Treap_iterator = self.root
        ascendents_stack = [] #Keeping all possible parents of the inserted node

        while (True):
            ascendents_stack.append(Treap_iterator)

            if node > Treap_iterator.key: 
                if (not Treap_iterator.right): #Inserting node at right of current node
                    Treap_iterator.right = new_node
                    return ascendents_stack, new_node
                
                Treap_iterator = Treap_iterator.right #Going to the right subtree
            elif node < Treap_iterator.key: 
                if (not Treap_iterator.left): #Inserting node at left of curr node
                    Treap_iterator.left = new_node
                    return ascendents_stack, new_node
                
                Treap_iterator = Treap_iterator.left #Going to the left subtree
            else: #No node gets inserted if it already exists
                return None, None

    #Makes rotations in oreder to keep the heap property
    def __bubbleUpPriority(self, ascendents_stack : List[Node], new_node : Node):
        while ascendents_stack:
            parent = ascendents_stack.pop()

            if ascendents_stack:
                grandparent = ascendents_stack[-1]
            else:
                grandparent = None

            #If the heap property is met then we stop
            if parent.priority >= new_node.priority:
                return

            if parent.right and parent.right.key == new_node.key: #Right child implies left rotation
                new_child = self.__leftRotation(parent)

            elif parent.left and parent.left.key == new_node.key: #Left child implies right rotation
                new_child = self.__rightRotation(parent)
            
            self.__fatherConnectionAfterRotation(grandparent, new_child)

    #Makes rotations in order to get the node to be a leaf and returns it's parent
    def __bubbleDownPriority(self, parent : Node, del_node : Node) -> Node:
        while (del_node.left or del_node.right):
            if not del_node.left:
                new_parent = self.__leftRotation(del_node)
            elif not del_node.right:
                new_parent = self.__rightRotation(del_node)
            elif del_node.right.priority > del_node.left.priority:
                new_parent = self.__leftRotation(del_node)
            else:
                new_parent = self.__rightRotation(del_node)
            
            self.__fatherConnectionAfterRotation(parent, new_parent)
            parent = new_parent
            
        return parent
            
    def __rightRotation(self, old_root : Node) -> Node:
        new_root = old_root.left
        new_root_right = new_root.right

        new_root.right = old_root
        old_root.left = new_root_right

        return new_root

    def __leftRotation(self, old_root : Node) -> Node:
        new_root = old_root.right
        new_root_left = new_root.left

        new_root.left = old_root
        old_root.right = new_root_left

        return new_root
    
    def __fatherConnectionAfterRotation(self, father_old_root : Node, new_root : Node):
        if father_old_root:
            if new_root.key > father_old_root.key:
                father_old_root.right = new_root
            else:
                father_old_root.left = new_root
        else: #No parent implies it has become the root
            self.root = new_root

    def __removeLeaf(self, parent_del_node : Node, del_node : Node):
        if not parent_del_node: #Removing the root as the only node
            self.root = None
        elif parent_del_node.left and parent_del_node.left.key == del_node.key:
            parent_del_node.left = None
        elif parent_del_node.right.key == del_node.key:
            parent_del_node.right = None