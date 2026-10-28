def knapsack(w, p, cap):
    n = len(w)
    dp = [[0]*(cap+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for c in range(cap+1):
            dp[i][c] = dp[i-1][c]
            if w[i-1] <= c:
                dp[i][c] = max(dp[i][c],
                    p[i-1] + dp[i-1][c-w[i-1]])

    print("Maximum profit:", dp[n][cap])

w = [10, 20, 30]
p = [60, 100, 120]
cap = 50

knapsack(w, p, cap)