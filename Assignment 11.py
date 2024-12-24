


# Implement a binary search tree (BST) and include methods for inserting nodes and searching for a value.

# Instructions:

    # 1. Implement a class Node that represents a node in the BST.
    # 2. Implement a class BinarySearchTree that supports inserting nodes and searching for a value.
    # 3. Write test cases to verify the implementation.



# Class to represent a Node in the Binary Search Tree
class Node:
    def __init__(self,value):
        self.value = value  # Value of the node
        self.left = None  # Left child
        self.right = None  # Right child

# Class to represent a Binary Search Tree (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None  # The root of the tree is initially None

    # Method to insert a value into the BST
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node  # If the tree is empty, the new node becomes the root
        else:
           self._insert_recursive(self.root, new_node)  # Insert recursively

    # Helper method for recursive insertion
    def _insert_recursive(self, current, new_node):
        if new_node.value < current.value:
            # Insert in the left subtree if the new value is smaller
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            # Insert in the right subtree if the new value is greater or equal
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    # Method to search for a value un the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method for recursive search
    def _search_recursive(self, current, value):
        if current is None:
            return False  # If we reach a leaf node and don't find the value
        if current.value == value:
            return True  # Found the value
        elif value < current.value:
            return self._search_recursive(current.left, value)  # Search left
        else:
            return self._search_recursive(current.right, value)  # Search right

# Test cases to verify the implementation
if __name__ == "__main__":
    # Create a Binary Search Tree and insert values
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Search for values
    print("Search for 40:", bst.search(40))  # Expected: True
    print("Search for 25:", bst.search(25))  # Expected: False
    print("Search for 70:", bst.search(70))  # Expected: True
    print("Search for 100:", bst.search(100))  # Expected: False