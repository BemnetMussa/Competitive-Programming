class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        max_subarry = sum(nums[:k])

        window = max_subarry
        for i in range(k, len(nums)):
     
            window -= nums[i-k]
            window += nums[i]
       


            if window > max_subarry:
                max_subarry = window

        return max_subarry / k

