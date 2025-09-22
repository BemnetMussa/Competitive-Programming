class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        frequency_nums = Counter(nums)

        total_max = 0
        max_frequency = max(frequency_nums.values())

        for value in frequency_nums.values():
            if max_frequency == value:
                total_max += max_frequency

        return total_max 