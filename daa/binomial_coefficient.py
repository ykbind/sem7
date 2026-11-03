# Binomial Coefficient using Dynamic Programming

def binomial(n, k):
    C = [[0 for j in range(k+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]


# Input
n = int(input("Enter n: "))
k = int(input("Enter k: "))

print("Binomial Coefficient:", binomial(n, k))


# Expected Input:
# Enter n: 5
# Enter k: 2

# Expected Output:
# Binomial Coefficient: 10