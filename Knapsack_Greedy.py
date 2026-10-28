def knapsack(w, p, cap):
    items = sorted(zip(w, p), key=lambda x: x[1]/x[0], reverse=True)
    profit = 0

    for weight, value in items:
        if cap >= weight:
            profit += value
            cap -= weight
        else:
            profit += value * cap / weight
            break

    print("Maximum profit:", profit)

w = [10, 20, 30]
p = [60, 100, 120]
cap = 50

knapsack(w, p, cap)