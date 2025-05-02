from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = Counter(nums)
        # turn it into a list of (num, freq) and sort by freq descending
        sorted_items = sorted(count_nums.items(), key=lambda x: x[1], reverse=True)
  
        return [num for num, freq in sorted_items[:k]]
