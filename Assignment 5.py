


# Implement a recursive function to calculate the factorial of a non-negative integer.

# Instructions:

    # 1. Write a recursive function factorial(n) that returns the factorial of the non-negative integer n.
    # 2. The factorial of n(denoted as n!) is defined as:
            # n!= n * (n-1)! for n > 0
            # 0!= 1
    # 3. Write test cases to verify the function works correctly for different values of n.


# Recursive function to calculate the factorial of n
def factorial(n):

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n-1)

# Test case to verify the correctness of the factorial function
print(factorial(0))   # Expected output: 1, as 0! = 1
print(factorial(1))   # Expected output: 1, as 1! = 1
print(factorial(2))   # Expected output: 2, as 2! = 2 * 1 = 2
print(factorial(3))   # Expected output: 6, as 3! = 3 * 2 * 1 = 6
print(factorial(4))   # Expected output: 24, as 4! = 4 * 3 * 2 * 1 = 24
print(factorial(5))   # Expected output: 120, as 5! = 5 * 4 * 3 * 2 * 1 = 120