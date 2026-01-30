class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:


        if t < 0 or k <= 0:
            return False
            
        window = SortedList()
        
        for i, num in enumerate(nums):
            # Find the smallest number >= num - t
            idx = window.bisect_left(num - t)
            
            # Check if there's a number in [num - t, num + t]
            if idx < len(window) and abs(window[idx] - num) <= t:
                return True
                
            window.add(num)
            
            # Keep window size <= k
            if len(window) > k:
                window.remove(nums[i - k])
        
        return False