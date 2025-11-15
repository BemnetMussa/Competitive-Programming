class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        res = set()

        # intension is to max with uniqueness
        for num in nums:
            if num > 0 and num not in res:
                res.add(num)

        if not res:
            return nums[0]

        return sum(res)