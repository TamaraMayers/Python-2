


# Implement a basic queue using Python's built in list data structure. The queue should support standard operations like enqueue, dequeue, and checking if the queue is empty.
# Instructions:

# 1. Implement a class Queue with the following methods:
#    enqueue(item): Add an item to the end of the queue.
#    dequeue(): Removes and returns the item at the front of the queue. If the queue is empty, it should raise an exception.
#    is_empty(): Returns True if the queue iss empty, False if otherwise.
#    size(): Returns the number of the items in the queue.

# 2.  Write a few test cases to demonstrate the functionality if the queue.



# Queue clss using a list to store the items
class Queue:
    def __init__(self):
        self.items = []   # Creates an empty list to hold queue items

    def enqueue(self,item):
        # Adds an item to the end of the queue
        self.items.append(item)   # Appends the item to the list, which is the end of the queue

    def dequeue(self):
        # Removes and returns the items at the front of the queue
        if self.is_empty():   # Checks if the queue is empty
           raise Exception("Queue is empty")   # If empty, raise an exception
        return self.items.pop(0)   # Removes the first item in the list (front of the queue) and returns it

    def is_empty(self):
        # Checks if the queue has any items
        return len(self.items) == 0   # Returns True if the list is empty, otherwise False

    def size(self):
        # Returns the number of items in the queue
        return len(self.items)   # Counts the number of items in the list

# Test cases to demonstrate the Queue class
if __name__ == "__main__":
    q = Queue()   # Creates a new empty queue

    # Testing enqueue
    q.enqueue(1)   # Adds 1 to the queue
    q.enqueue(2)   # Adds 2 to the queue
    q.enqueue(3)   # Adds 3 to the queue
    print("Queue after enqueueing 1,2,3: ", q.items)   # Should display: [1, 2, 3]

    # Testing dequeue
    print("Dequeued item: ", q.dequeue())   # Removes and prints the first item (1)
    print("Queue after one dequeue: ", q.items)   # Should display [2, 3]

    # Testing is_empty and size
    print("Is the queue empty? ", q.is_empty())   # Should return False, queue still has items
    print("Size of the queue: ", q.size())   # Should return 2, as two items (2 and 3) are left in the queue

    # Testing dequeue on remaining items
    print("Dequeued item: ", q.dequeue())   # Removes and prints the first item (2)
    print("Dequeued item: ", q.dequeue())   # Removes and prints the first item (3)

    # Testing is_empty on empty queue
    print("Is the queue empty after all dequeues? ", q.is_empty())   # Should return True, queue is empty now

    # Testing dequeue on an empty queue to raise exception
    try:
        q.dequeue()   # Attempts to dequeue from an empty queue, which should raise an exception
    except Exception as e:
        print("Exception: ", e)   # Prints the exception message