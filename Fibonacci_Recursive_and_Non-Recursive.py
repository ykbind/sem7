import time

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

n = int(input("Enter n: "))

print("Iterative:")
fib_iter(n)

print("\nRecursive:")
for i in range(n):
    print(fib_rec(i), end=" ")

print("\nIterative: Time O(n), Space O(1)")
print("Recursive: Time O(2^n), Space O(n)")