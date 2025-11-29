x = int(input().strip())

'''
x = a(a+1)/ 2 + b (b+1) 2

approch:
hold all the trangular possiblities 
check if ..
'''


triangular_nums = set()

k = 1
while True:
    t = k * (k + 1) // 2
    if t > x:
        break
    triangular_nums.add(t)
    k += 1

for tri in triangular_nums:
    if (x - tri) in triangular_nums:
        print("YES")
        break
        
else:
    print("NO")
