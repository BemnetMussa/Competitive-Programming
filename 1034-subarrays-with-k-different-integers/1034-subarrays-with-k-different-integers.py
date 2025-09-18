from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            freq = defaultdict(int)
            left = 0
            count = 0
            for right, num in enumerate(nums):
                freq[num] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                count += right - left + 1
            return count
        
        return atMost(k) - atMost(k - 1)
