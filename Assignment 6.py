


# Implement a recursive function to compute the nth Fibonacci number.

# Instructions:

    # 1. Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
    # 2. The Fibonacci sequence is defined as:
            # F(0) = 0
            # F(1) = 1
            # F(n) = F(n - 1) + F(n - 2) for n > 1

    # 3. Write test cases to verify the function works correctly for different values of n.



# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base case: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case: Fibonacci of n is the sum of the previous two Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci( n - 2)

# Test cases to verify the correctness of the Fibonacci function
print(fibonacci(0))   # Expected output: 0, as F(0) = 0
print(fibonacci(1))   # Expected output: 1, as F(1) = 1
print(fibonacci(2))   # Expected output: 1, as F(2) = F(1) + F(0) = 1 + 0 = 1
print(fibonacci(3))   # Expected output: 2, as F(3) = F(2) + F(1) = 1 + 1 = 2
print(fibonacci(4))   # Expected output: 3, as F(4) = F(3) + F(2) = 2 + 1 = 3
print(fibonacci(5))   # Expected output: 5, as F(5) = F(4) + F(3) = 3 + 2 = 5
print(fibonacci(6))   # Expected output: 8, as F(6) = F(5) + F(4) = 5 + 3 = 8