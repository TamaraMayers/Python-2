


# Use Python's collections.deque to implement a more efficient queue.

# Instructions

# 1.   Implement a class DequeQueue with the following methods:
            #enqueue(item): Adds an item to the end of the queue.
            # dequeue(): Removes and returns the item at the front of the queue. If the is empty, it should raise an exception.
            # is_empty(): Returns True if the queue is empty, False if otherwise.
            # size(): Returns the number of items in the queue.

# 2.    Write a few test cases to demonstrate the functionality of the queue.



from collections import deque   # Implementing deque for efficient queue operations

# DequeQueue clss using deque to implement a queue
class DequeQueue:
    def __init__ (self):
        self.queue = deque()   # Creates an empty deque to hold the queue items

    def enqueue(self, item):
        # Adds an item to the end of the queue
        self.queue.append(item)   # Appends the item to the queue (efficient operation)

    def dequeue(self):
        # Removes and returns the item at the front of the queue
        if self.is_empty():  # Checks if the queue is empty
            raise Exception("Queue is empty")  # If empty, raise an exception
        return self.queue.popleft()  # Removes and returns the first item (front of the queue)

    def is_empty(self):
        # Checks if the queue has any items
        return len(self.queue) == 0   # Return True if the deque is empty, otherwise False

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)  # Returns the length of the deque

# Test cases to demonstrate the DequeQueue class
if __name__ == "__main__":
    dq = DequeQueue()  # Creates a new empty queue using deque

    # Testing enqueue
    dq.enqueue(1)  # Adds 1 to the queue
    dq.enqueue(2)  # Adds 2 to the queue
    dq.enqueue(3)  # Adds 3 to the queue
    print("Queue after enqueueing 1, 2, 3:", list(dq.queue))  # Should display: [1, 2, 3]

    # Testing dequeue
    print("Dequeued item: ", dq.dequeue())   # Removes and prints the first item (1)
    print("Queue after one dequeue: ", list(dq.queue))   # Should display: [2, 3]

    # Testing is_empty and size
    print("Is the queue empty? ", dq.is_empty())   # Should return False, as queue still has items
    print("Size of the queue: ", dq.size())   # Should return 2, as two items (2 and 3) are left in the queue

    # Testing dequeue on remaining items
    print("Dequeued item: ", dq.dequeue())   # Removes and prints the first item (2)
    print("Dequeued item: ", dq.dequeue())   # Removes and prints the first item (3)

    # Testing is_empty on an empty queue
    print("Is the queue empty after all dequeues? ", dq.is_empty())   # Should return True, queue is empty now

    #Testing dequeue on an empty queue to raise exception
    try:
        dq.dequeue()   # Attempts to dequeue from an empty queue, which should raise an exception
    except Exception as e:
        print("Exception: ", e)   # Prints the exception message
