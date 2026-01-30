numTestCases = int(input())

def bad(last4, x):
    a = last4 + [x]
    inc = True
    dec = True

    for i in range(4):
        if a[i] >= a[i+1]:
            inc = False
        if a[i] <= a[i+1]:
            dec = False

    return inc or dec


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    answer = []
    last = []
    left, right = 0, n - 1

    for _ in range(n):
        lv = nums[left]
        rv = nums[right]

        if len(last) < 4 or not bad(last, lv):
            answer.append("L")
            last.append(lv)
            left += 1
        else:
            answer.append("R")
            last.append(rv)
            right -= 1

        if len(last) > 4:
            last.pop(0)

    print("".join(answer))


for _ in range(numTestCases):
    solve()
