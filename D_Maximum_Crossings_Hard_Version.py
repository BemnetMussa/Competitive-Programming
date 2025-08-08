def count_crossings(a):
    n = len(a)
    max_val = max(a)

    # Binary Indexed Tree (Fenwick Tree)
    bit = [0] * (max_val + 2)  # +2 to be safe

    def update(index, value):
        while index <= max_val:
            bit[index] += value
            index += index & -index

    def query(index):
        res = 0
        while index > 0:
            res += bit[index]
            index -= index & -index
        return res

    crossings = 0
    for i in range(n):
        x = a[i]
        crossings += i - query(x - 1)
        update(x, 1)

    return crossings

# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_crossings(a))
