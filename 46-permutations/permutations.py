class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def dfs(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    arr.pop()

            return ans

        return dfs([])
