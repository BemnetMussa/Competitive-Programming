


a = list(input())
q = int(input())


ans = []
for _ in range(q):
    k, l, r = list(input().split())
    if k == "2":
        unique = set()
        
        for i in range(int(l)-1, int(r)):
            unique.add(a[i])

        ans.append(len(unique))

    else:
        for i in range(int(k)-1, int(l)):
            a[i] = r

for a in ans:
    print(a)