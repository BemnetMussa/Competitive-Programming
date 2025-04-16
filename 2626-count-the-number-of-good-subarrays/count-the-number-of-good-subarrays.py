class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        seen = collections.Counter()
        pairs = 0
        total = 0
        
        left = 0
        for right in range(len(nums)):
            pairs += seen[nums[right]]
            seen[nums[right]] += 1

            while pairs >= k:
                seen[nums[left]] -= 1
                pairs -= seen[nums[left]]
                left += 1

            total += left

        return total