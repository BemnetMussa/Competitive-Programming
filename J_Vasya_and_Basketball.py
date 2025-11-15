from bisect import bisect_left
n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

mx=3*n
mn=3*m

arr1.sort()
arr2.sort()
ans=mx-mn
ans1=mx
ans2=mn
a=0
b=0
for i in range(arr1[0],arr1[-1]+1):
    i2=bisect_left(arr2,i)
    i3=bisect_left(arr1,i)
    mxn=mx-i3
    mnn=mn-i2
    # print(mxn, mnn)
    if mxn-mnn>ans1-ans2:
        ans1=mxn
        ans2=mnn

print(str(ans1)+':'+str(ans2))


