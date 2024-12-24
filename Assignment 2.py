


# Removing a Node from a Singly List
# Task: Implement a method remove(data) in the LinkedList class that removes the first occurrence of a node with the specified data from the list.



# Node class remains the same from Assignment 1

class Node:
    def __init__(self,data):
        self.data = data   # Stores the data in this item
        self.next = None   # Points to the next item in the list, or None if it's the last item

class SinglyLinkedList:
    def __init__(self):
        self.head = None   # Keeps track of the first item in the list; None if the list is empty

    def append(self,data):
        new_node = Node(data)   # Creates a new item with the given data
        if not self.head:   # Checks if the list is empty
            self.head = new_node   # If empty, set the new item as the first item (head)
        else:
            last_node = self.head   # Starts at the first item to find the end of the list
            while last_node.next:   # Keeps moving to the next item until the last one
                last_node = last_node.next
            last_node.next = new_node   # Link the last item to the new item

    def prepend(self,data):
        new_node = Node(data)   # Creates a new item with the given data
        new_node.next = self.head   # Points the new item to the current first item (head)
        self.head = new_node     # Updates the head to the new item

    def print_list(self):
        current_node = self.head    # Starts at the first item
        while current_node:    # Continues as long as there are items left
            print(current_node.data, end=" -> ")    # Prints the data in the current item
            current_node = current_node.next    # Moves to the next item
        print("None")    # Shows the end of the list

    # Remove method
    # Finds and removes the first item with the specified data from the list
    def remove(self,data):
        if not self.head:   # Checks if the list is empty
            return   # If it's empty, there's nothing to remove

        # Check if the head (first item) is the one to remove
        if self.head.data == data:
            self.head = self.head.next   # Moves the head to the next item
            return

        # Otherwise, look for the item in the rest of the list
        current_node = self.head   # Starts with the first item
        while current_node.next:   #Goes through each item until the end
            if current_node.next.data == data:   # Checks if the next item has the data to remove
                current_node.next = current_node.next.next   # Skips the item to remove it
                return   # Exits the method once the item is removed
            current_node = current_node.next   # Moves to the next item

# Usage example with the remove method
if __name__ == "__main__":
    sll = SinglyLinkedList()    # Creates a new empty linked list
    sll.append(1)   # Adds an item with data 1 to the end
    sll.append(2)   # Adds an item with data 2 to the end
    sll.append(3)   # Adds an item with data 3 to the end
    sll.print_list()   # Shows all the items' expected output: 1 -> 2 -> 3 -> None

    sll.remove(2)   # Removes the item with data 2
    sll.print_list()   # Shows remaining items; expected output 1 -> 3 -> None