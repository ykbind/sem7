# Fractional Knapsack using Greedy Algorithm

def knapsack(w, p, cap):
    items = sorted(
        zip(w, p),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    profit = 0

    for weight, value in items:
        if cap >= weight:
            profit += value
            cap -= weight
        else:
            profit += value * cap / weight
            break

    print("Maximum profit:", profit)


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
# Maximum profit: 240.0