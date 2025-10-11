


n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))


xy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def check(x, y):

    ans = 0
    for i in range(x, len(xy)):
        if xy[i] == y:
           
            ans = abs(i - x)
            break

    return ans
    


total  =0
for i in range(n):
    ans1 = check(a[i], b[i])
    ans2 = check(b[i], a[i])


    total += min([ans1, ans2])


print(total)
