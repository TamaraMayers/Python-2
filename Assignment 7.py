


# How would you implement the Bubble Sort algorithm in Python to sort a list of numbers in ascending order?
    # Give an example.



# Function to perform Buble Sort on a list
def bubble_sort(arr):
    n = len(arr)

    # Transverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]   # Swap the elements

# Example to demonstrate the Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", arr)

# Call the bubble_sort function
bubble_sort(arr)

print("Sorted list:", arr)