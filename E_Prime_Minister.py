n = int(input())
a = [int(i) for i in input().split()]

alice = a[0]
total_sum = sum(a)
half = (total_sum // 2)



curr_sum = alice
res = [1]
flag = False


for i in range(1, n):
    # print(a[i], alice, half)
    if a[i] * 2 <= alice:
        res.append(i + 1)
        curr_sum += a[i] 
    
    if curr_sum > half:
        flag = True
      

    if curr_sum > half:
        break
    
# print(res, flag)
if flag:
    print(len(res))
    print(*res)
else:
    print(0)