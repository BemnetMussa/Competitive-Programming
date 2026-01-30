
strA = input().strip()
check = "hello"
k = 0
for i in range(len(strA)):
    if strA[i] == check[k]:
        k += 1
        if k == len(check):
            break

print("YES" if k == len(check) else "NO")

