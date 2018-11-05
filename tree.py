class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree Class
class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value=value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value=value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value=value)
            else:
                self._insert(value, current_node.right)
        else:
            print("value already in tree")

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left, current_height+1)
        right_height = self._height(current_node.right, current_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value is current_node.value:
            return True
        elif (value < current_node.value) and (current_node.left is not None):
            return self._search(value, current_node.left)
        elif (value > current_node.value) and (current_node.right is not None):
            return self._search(value, current_node.right)
        return False

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left)
            print("value at current node is:", current_node.value )
            self._print_tree(current_node.right)


tree = BST()
tree.insert(8)
tree.insert(7)
tree.insert(10)
tree.insert(5)
tree.insert(12)
tree.insert(9)
tree.insert(13)
tree.print_tree()
print(tree.search(13))