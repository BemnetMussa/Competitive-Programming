from functools import lru_cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # dp(left, right) returns the maximum score difference the current player can achieve 
        # from the subarray nums[left:right+1]
        @lru_cache(maxsize=None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            # The current player can choose either end:
            # They add the chosen number and subtract the opponent's best response.
            score_left = nums[left] - dp(left + 1, right)
            score_right = nums[right] - dp(left, right - 1)
            return max(score_left, score_right)
        
        # If the maximum difference is non-negative, player1 wins or ties (which counts as a win)
        return dp(0, n - 1) >= 0
