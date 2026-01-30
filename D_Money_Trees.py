t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))

    left = 0
    curr_sum = 0
    ans = 0

    for right in range(n):

        # if height chain breaks, restart window
        if right > 0 and h[right-1] % h[right] != 0:
            left = right
            curr_sum = 0

        curr_sum += a[right]

        # if sum too large, shrink from left
        while curr_sum > k:
            curr_sum -= a[left]
            left += 1

        ans = max(ans, right - left + 1)

    print(ans)
    