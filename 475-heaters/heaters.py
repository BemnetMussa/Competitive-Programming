def possibility(arr,pr,heat):
    k = 0
    ans =[]
    i = 0
    while i<len(arr):
        if arr[i]<heat[k]-pr:
            return False
        if arr[i]>heat[k]+pr:
            k+=1
            if k==len(heat):
                return False
        else:
            i+=1
    return True

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l=0
        r = int(1e9)
        if len(houses)==1:
            return 0

        while l<=r:
            mid = l+(r-l)//2
            if possibility(houses,mid,heaters):
                r = mid-1
            else:
                l = mid+1
        return l
        