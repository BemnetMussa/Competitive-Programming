class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cleaned = [nums[0]]
        for num in nums[1:]:
            if num != cleaned[-1]:
                cleaned.append(num)

        
        count = 0
        for i in range(1, len(cleaned) - 1):
            if cleaned[i] > cleaned[i-1] and cleaned[i] > cleaned[i+1]:
                count += 1  # hill
            elif cleaned[i] < cleaned[i-1] and cleaned[i] < cleaned[i+1]:
                count += 1  # valley
        return count