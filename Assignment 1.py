


# Task:  Implement a singly linked list class with the following methods:
# append(data): Adds a new node with the specific data at the end of the list.
# prepend(data): Adds a new node with the specified data at the beginning of the list.
# print_list(): Prints all the elements in the list.


# Node class
# Creates each item in the list
# Stores data and a link to the next item
class Node:
    def __init__(self,data):
        self.data = data     # Stores the data in this item
        self.next = None     # Points to the next item in the list, or None if it's the last item

# SinglyLinkedList class
# Organizes and keeps track of all the items in the list
# Points to the first item in the list (called the "head"

class SinglyLinkedList:
    def __init__(self):
        self.head = None # Keeps track of the first item in the list; None if the list is empty

    # Append method
    # Adds a new item to the end of the list
    # Works if the list is empty or has items

    def append(self,data):
        new_node = Node(data)    # Creates a new item with the given data
        if not self.head:   # Checks if the list is empty
            self.head = new_node    # If empty, set the new item as the first item (head)
        else:
            last_node = self.head   # Starts at the first item to find the end of the list
            while last_node.next:   # Keeps moving to the next item until the last one
                last_node = last_node.next
            last_node.next = new_node   # Link the last item to the new item

    # Prepend method
    # Adds a new item to the beginning of the list
    # Updates the head to the new item

    def prepend(self,data):
        new_node = Node(data)   # Creates a new item with the given data
        new_node.next = self.head   # Points the new item to the current first item (head)
        self.head = new_node    # Updates the head to the new item

    # Print List method
    # Goes through each item and shows the data in order
    # Stops when there are no more items

    def print_list(self):
        current_node = self.head   # Starts at the first item
        while current_node:   # Continues as long as there are items left
            print(current_node.data, end=" -> ")   #Prints the data in the current item
            current_node = current_node.next    # Moves to the next item
        print("None")   # Shows the end of the list

# Usage example
# Demonstrates how to use the linked list
# Tests adding items to the start and end, and printing the list

if __name__== "__main__":
    sll = SinglyLinkedList()   # Creates a new empty linked list
    sll.append(1)   # Adds an item with data 1 to the end
    sll.append(2)   # Adds an item with data 2 to the end
    sll.prepend(0)  # Adds an item with data 0 to the start
    sll.print_list()   # Shows all the items from start to end; expected output is 0 -> 1 -> 2 -> None