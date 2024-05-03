from utils.Trees.Tree import Node, Tree


def right_rotate(pivot):
    subTree = pivot.left
    pivot.left = subTree.right
    subTree.right = pivot

    return subTree


def left_rotate(pivot):
    subTree = pivot.right
    pivot.right = subTree.left
    subTree.left = pivot

    return subTree


class SplayTree(Tree):
    root = Node(-1)

    def splay(self, root, key):
        if not root or root.key == key:
            return root

        if root.key > key:
            if not root.left:
                return root

            if root.left.key > key:
                root.left.left = self.splay(root.left.left, key)
                root = right_rotate(root)

            else:
                if root.left.key < key:
                    root.left.right = self.splay(root.left.right, key)

                    if root.left.right:
                        root.left = left_rotate(root.left)

            return not root.left and root or right_rotate(root)

        else:
            if root.right is None:
                return root

            if root.right.key > key:
                root.right.left = self.splay(root.right.left, key)

                if root.right.left:
                    root.right = right_rotate(root.right)

            else:
                if root.right.key < key:
                    root.right.right = self.splay(root.right.right, key)
                    root = left_rotate(root)

            return not root.right and root or left_rotate(root)

    def search(self, node):
        return self.inner_search(self.root, node)

    def insert(self, node):
        return bool(self.inner_insert(self.root, node))

    def remove(self, node):
        return bool(self.inner_remove(self.root, node))

    def inner_search(self, root, key):
        return self.splay(root, key)

    def inner_insert(self, root, key):
        if root is None:
            return Node(key)

        root = self.splay(root, key)

        if root.key == key:
            return root

        if root.key > key:
            new_node = Node(key)
            new_node.right = root
            new_node.left = root.left
            root.left = None

            self.root = new_node
            return new_node

        else:
            new_node = Node(key)
            new_node.left = root
            new_node.right = root.right
            root.right = None

            self.root = new_node
            return new_node

    def inner_remove(self, root, key):
        if root is None:
            return root

        root = self.splay(root, key)

        if root.key != key:
            return root

        if root.left is None:
            new_root = root.right

        else:
            new_root = self.splay(root.left, key)
            new_root.right = root.right

        self.root = new_root
        return new_root

    def meetsRequirments(self) -> bool:
        return True
