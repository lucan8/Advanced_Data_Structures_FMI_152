from utils.Trees.Tree import Node

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


class SplayTree:
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

    def search(self, root, key):
        return self.splay(root, key)

    def insert(self, root, key):
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

            return new_node

        else:
            new_node = Node(key)
            new_node.left = root
            new_node.right = root.right
            root.right = None

            return new_node

    def remove(self, root, key):
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

        return new_root
