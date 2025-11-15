class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)

        dp1=[1]*(n)

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                dp1[i]=1+dp1[i-1]
        dp2=[1]*n
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                dp2[i]=1+dp2[i+1]
        sum=0
        for i in range(n):
            sum+=max(dp1[i],dp2[i])
        return sum
            