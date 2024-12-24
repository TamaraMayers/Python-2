


# What is the time complexity of the Quick Sort algorithm, and how would you implement it in Python?
# Give an example.



# Function to perform Quick Sort
def quick_sort(arr):
    # Base case: if the list is empty or has one element, it's already sorted
    if len(arr) <=1:
        return arr
    else:
        # Choose a pivot (we're choosing the last element in this case)
        pivot = arr[-1]

        # Partition the array into two sub arrays:
        # - Left of pivot: elements smaller than pivot
        # - Right of pivot: elements greater than pivot
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        # Recursively apply quick_sort to the left and right parts, and combine
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example to demonstrate Quick Sort
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", arr)

# Call the quick_sort function
sorted_arr = quick_sort(arr)

print("Sorted list:", sorted_arr)