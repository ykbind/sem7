def solve(n, row=0, cols=[]):
    if row == n:
        for r in range(n):
            print(" ".join("Q" if c == cols[r] else "." for c in range(n)))
        return True

    for c in range(n):
        if c in cols or any(abs(cols[r]-c) == row-r for r in range(row)):
            continue
        cols.append(c)
        if solve(n, row+1, cols):
            return True
        cols.pop()

    return False

n = int(input("Enter N: "))
first = int(input("First queen column (0 to N-1): "))

solve(n, 1, [first])