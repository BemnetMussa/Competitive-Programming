import bisect

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ans = 0

        # Fix i (largest of the 3), and try j < i
        for i in range(n):
            for j in range(i):
                # Calculate the threshold that a[k] must exceed
                threshold = max(2 * a[i], a[-1]) - a[i] - a[j]

                # Find first index k < j such that a[k] > threshold
                k = bisect.bisect_right(a, threshold, 0, j)

                # Count how many valid k's are there
                ans += j - k

        print(ans)
solve()