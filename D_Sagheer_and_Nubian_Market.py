import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    # Validity check
    if k % 2 == 0 or k > 2 * n - 1:
        print(-1)
        return

    a = list(range(1, n + 1))
    need = (k - 1) // 2  # number of swaps needed

    i = 0
    while need > 0 and i + 1 < n:
        a[i], a[i + 1] = a[i + 1], a[i]
        need -= 1
        i += 2

    print(*a)

if __name__ == "__main__":
    solve()
