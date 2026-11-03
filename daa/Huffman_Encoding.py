# Huffman Coding using Greedy Algorithm

import heapq

def huffman(char, freq):
    heap = [[f, [c, ""]] for c, f in zip(char, freq)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for x in left[1:]:
            x[1] = '0' + x[1]

        for x in right[1:]:
            x[1] = '1' + x[1]

        heapq.heappush(
            heap,
            [left[0] + right[0]] + left[1:] + right[1:]
        )

    return heapq.heappop(heap)[1:]


# Input
n = int(input("Enter number of characters: "))

char = []
freq = []

for i in range(n):
    c = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of {c}: "))
    char.append(c)
    freq.append(f)

# Generate Huffman Codes
codes = huffman(char, freq)

print("\nHuffman Codes:")
for c, code in codes:
    print(c, ":", code)


# Expected Input:
# Enter number of characters: 6
# Enter character 1: A
# Enter frequency of A: 5
# Enter character 2: B
# Enter frequency of B: 9
# Enter character 3: C
# Enter frequency of C: 12
# Enter character 4: D
# Enter frequency of D: 13
# Enter character 5: E
# Enter frequency of E: 16
# Enter character 6: F
# Enter frequency of F: 45

# Expected Output (one possible valid result):
# Huffman Codes:
# F : 0
# C : 100
# D : 101
# A : 1100
# B : 1101
# E : 111