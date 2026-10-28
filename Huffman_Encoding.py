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

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    return heapq.heappop(heap)[1:]

char = ['A', 'B', 'C', 'D', 'E', 'F']
freq = [5, 9, 12, 13, 16, 45]

codes = huffman(char, freq)

for c, code in codes:
    print(c, ":", code)