


# Implement a basic binary tree and include methods for in-order, pre-order, and post-order traversal.
#Instructions:

    # 1. Implement a class Node that represents a node in the binary tree.
    # 2. Implement a class BinaryTree that supports inserting nodes and three types of traversal methods: in-order, pre-order, and post-order.
    # 3. Write test cases to verify the implementation.



# Class to represent a Node in the binary tree
class Node:
    def __init__(self, value):
        self.value = value      # The value of the node
        self.left = None        # Left child
        self.right = None       # Right child

# Class to represent a Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None    # Initialize an empty tree

    # Method to insert a node into the binary tree
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node    # If the tree is empty, the new node becomes the root
        else:
            self._insert_recursive(self.root, new_node)     # Call the helper method to insert recursively

    # Helper method for recursive insertion
    def _insert_recursive(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    # In-order traversal: Left -> Node -> Right
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    # Pre-order traversal: Node -> Left -> Right
    def pre_order(self, node):
        if node:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Post-order traversal: Left -> Right -> Node
    def post_order(self,node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=" ")

# Test cases to verify the implementation
if __name__ == "__main__":
    # Create a binary tree and insert values
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("In-order traversal:")
    tree.in_order(tree.root)    # Expected: 20 30 40 50 60 70 80
    print("\nPre-order traversal:")
    tree.pre_order(tree.root)   # Expected: 50 30 20 40 70 60 80
    print("\nPost-order traversal:")
    tree.post_order(tree.root)  # Expected: 20 40 30 60 80 70 50