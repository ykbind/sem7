# Fibonacci Series using Iterative and Recursive Methods

import time

# Iterative Method
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Recursive Method
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


# Input
n = int(input("Enter n: "))

print("Iterative:")
fib_iter(n)

print("\nRecursive:")
for i in range(n):
    print(fib_rec(i), end=" ")


# Time and Space Complexity
print("\nIterative: Time O(n), Space O(1)")
print("Recursive: Time O(2^n), Space O(n)")


# Expected Input:
# Enter n: 7

# Expected Output:
# Iterative:
# 0 1 1 2 3 5 8
#
# Recursive:
# 0 1 1 2 3 5 8
#
# Iterative: Time O(n), Space O(1)
# Recursive: Time O(2^n), Space O(n)