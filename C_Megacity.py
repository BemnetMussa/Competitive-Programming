import math
n,s=map(int,input().split())

arr=[]

for _ in range(n):
    x,y,k=map(int,input().split())
    arr.append([x,y,k])


left=0
right=10**5
tol=10**(-6)

target=10**6-s
# print(target)

def calc(x,y):
    return math.sqrt(x**2+y**2)

def check(r):
    pop=0
    for x,y,k in arr:
        if calc(x,y)-r<=tol:
            pop+=k
    return pop>=target

while right-left>=tol:
    # print
    m=(right+left)/2
    if check(m):
        right=m-tol
    else:
        left=m+tol
print((left) if check(left) else -1 )

