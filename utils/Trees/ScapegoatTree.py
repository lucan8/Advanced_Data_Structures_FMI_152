import math
from queue import Queue
from utils.Trees.Tree import Node, Tree

class GoatNode(Node):
    def __init__(self, key: int):
        super().__init__(key)
        self.parent = None

class ScapegoatTree(Tree):
    # alpha is a value between 0.5 and 1.0. It is responsible for how often balances
    # are done.
    def __init__(self, alpha: float):
        self.root = None
        self.size = 0
        self.max_size = 0
        self.alpha = alpha

    def search(self, node: int) -> GoatNode:
        curr_root = self.root
        while curr_root != None:
            if curr_root.key == node:
                break;

            if curr_root.key > node:
                curr_root = curr_root.left
            else:
                curr_root = curr_root.right

        return curr_root

    # returns the size of the subtree rooted at root
    def _subtree_size(self, root: GoatNode) -> int:
        if root == None:
            return 0
        return 1 + self._subtree_size(root.left) + self._subtree_size(root.right)

    # returns the node with the smallest key
    def _min_node(self, root: GoatNode) -> GoatNode | None:
        node = root
        while node.left != None:
            node = node.left
        return node

    # inserts a new node, if the node already exists
    # no insertion will be done
    def insert(self, node: int) -> bool:
        new_node = GoatNode(node)

        if self.search(new_node.key) != None:
            return False

        if self.root == None:
            self.root = new_node
            return True

        curr_node = self.root
        depth = 0
        possible_parent = None
        while curr_node != None:
            possible_parent = curr_node
            if new_node.key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            depth += 1

        new_node.parent = possible_parent
        if new_node.key < new_node.parent.key:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node

        self.size += 1
        self.max_size += 1

        # check for balanceing
        if depth > math.log(self.max_size, self.alpha):
            scapegoat = self._find_scapegoat(new_node)
            if scapegoat == None:
                return True

            tmp = self._rebalance(scapegoat)

            scapegoat.left = tmp.left
            scapegoat.right = tmp.right
            scapegoat.key = tmp.key

            if scapegoat.left != None:
                scapegoat.left.parent = scapegoat

            if scapegoat.right != None:
                scapegoat.right.parent = scapegoat

        return True

    def _find_scapegoat(self, node: GoatNode):
        scapegoat = node
        while 3 * self._subtree_size(scapegoat) <= 2 * self._subtree_size(scapegoat.parent):
            scapegoat = scapegoat.parent
        return scapegoat

    def _flatten(self, node: GoatNode, nodes):
        if node == None:
            return
        self._flatten(node.left, nodes)
        nodes.append(node)
        self._flatten(node.right, nodes)

    def _build_tree_from_list(self, nodes, start: int, end: int):
        if start > end:
            return
        mid = int(start + (end - start) / 2.0)
        node = GoatNode(nodes[mid].key)
        node.left = self._build_tree_from_list(nodes, start, mid - 1)
        node.right = self._build_tree_from_list(nodes, mid + 1, end)
        return node

    def _rebalance(self, root: GoatNode):
        nodes = []
        self._flatten(root, nodes)
        return self._build_tree_from_list(nodes, 0, len(nodes) - 1)

    def _remove(self, key: int) -> bool:
        # min_key_node = self._min_node()
        parent = None
        curr_node = self.root
        while curr_node != None and curr_node.key != key:
            parent = curr_node
            if key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        # key not found
        if curr_node == None:
            return False

        # [1] The found node has no children
        if curr_node.left == None and curr_node.right == None:
            if curr_node == self.root:
                self.root = None
            else:
                # check on witch side the node is
                if parent.left == curr_node:
                    parent.left = None
                else:
                    parent.right = None
            return True
        # [2] The found node has 2 children
        if curr_node.left != None and curr_node.right != None:
            successor = self._min_node(curr_node.right)
            curr_key = successor.key
            self.remove(successor.key)
            curr_node.key = curr_key

        # [3] The found node has 1 children
        child = None
        if curr_node.left != None:
            child = curr_node.left
        else:
            child = curr_node.right

        if curr_node == self.root:
            self.root = child
        else:
            if curr_node == parent.left:
                parent.left = child
            else:
                parent.right = child
        return True

    def remove(self, node: int) -> bool:
        removed = self._remove(node)
        if removed:
            self.size -= 1
            if self.size <= self.max_size // 2:
                self.root = self._rebalance(self.root)
                self.max_size = self.size
        return removed

    def meetsRequirments(self):
        if not (self.max_size // 2 <= self.size and self.size <= self.max_size):
            return False

        if not self.root:
            return True

        q = Queue()
        q.put(self.root)

        while not q.empty():
            elem = q.get()

            if elem.left:
                if elem.left.key >= elem.key:
                    return False

                q.put(elem.left)

            if elem.right:
                if elem.right.key <= elem.key:
                    return False

                q.put(elem.right)
        return True

