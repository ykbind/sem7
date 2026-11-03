# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(w, p, cap):
    n = len(w)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(cap + 1):
            dp[i][c] = dp[i-1][c]

            if w[i-1] <= c:
                dp[i][c] = max(
                    dp[i][c],
                    p[i-1] + dp[i-1][c-w[i-1]]
                )

    print("Maximum profit:", dp[n][cap])


# Input
n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    profit = int(input(f"Enter profit of item {i+1}: "))
    w.append(weight)
    p.append(profit)

cap = int(input("Enter knapsack capacity: "))

knapsack(w, p, cap)


# Expected Input:
# Enter number of items: 3
# Enter weight of item 1: 10
# Enter profit of item 1: 60
# Enter weight of item 2: 20
# Enter profit of item 2: 100
# Enter weight of item 3: 30
# Enter profit of item 3: 120
# Enter knapsack capacity: 50

# Expected Output:
# Maximum profit: 220