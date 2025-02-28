class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        pos = nums.index(k)
        rep_count = defaultdict(int)

        bal = 0
        for i in range(pos, len(nums)):
            bal += 1 if nums[pos] < nums[i] else (-1 if nums[pos] > nums[i] else 0)
            rep_count[bal] += 1
        
        bal = 0
        ans = 0
        for i in range(pos, -1, -1):
            bal += 1 if nums[pos] < nums[i] else (-1 if nums[pos] > nums[i] else 0)

            # for odd
            ans += rep_count[-bal]
            # for even
            ans += rep_count[-bal + 1]


        return ans
