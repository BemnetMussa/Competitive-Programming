
from collections import Counter
n = int(input())
a =  list(input())

q = int(input())
queries = []

for i in range(q):
    x, b = map(int, input().split())
    queries.append((x, b))

hashMap = Counter(a)

def solve():
    res = []

    if hashMap['+'] == hashMap['-']:
        res = ["YES"] * q
        return res


    for a , b in queries:
        if (a % b == 0 or b % a == 0) and a != b:
            res.append("YES")
            continue
        if hashMap["+"] % a == 0 and hashMap["-"] % b == 0:
            res.append("YES")

        elif hashMap["+"] % a == 0 and hashMap["-"] % a == 0:
            res.append("YES")
        elif hashMap["+"] % b == 0 and hashMap["-"] % b == 0:
            res.append("YES")

        elif hashMap["+"] % b == 0 and hashMap["-"] % a == 0:
            res.append("YES")
        
        else:
            res.append("NO")

    return res

req_ans = solve()
for ans in req_ans:
    print(ans)

    
