class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def gamE(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            score_left = nums[left] - gamE(left + 1, right)
            score_right = nums[right] - gamE(left, right - 1)
            return max(score_left, score_right)
        

        return gamE(0, n - 1) >= 0
