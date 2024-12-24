


# Explain the Merge Sort algorithm and demonstrate its implementation in Python to sort a list of strings in alphabetical order.
    # Give an example.



# Merge Sort function
def merge_sort(arr):
    # Base case: If the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_half, right_half)

# Helper function to merge two sorted lists
def merge(left, right):
    sorted_list = []
    while left and right:
        if left [0] < right [0]:    # Compare the first element of each list
            sorted_list.append(left.pop(0))     # Take the smaller element
        else:
            sorted_list.append(right.pop(0))    # Take the smaller element

    # Add any remaining elements from either list
    sorted_list.extend(left)
    sorted_list.extend(right)

    return sorted_list

# Example to demonstrate Merge Sort on a list of strings
arr = ["banana", "apple", "cherry", "date", "elderberry", "fig", "grape"]
print("Original list:", arr)

# Call the merge_sort function
sorted_arr = merge_sort(arr)

print("Sorted list in alphabetical order:", sorted_arr)