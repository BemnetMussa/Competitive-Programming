class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
            slide along the way count the max of the origianl nums
        [1,3,2,3,3] 2 + 2 * 1 +  2 * 1 = 6
         _______    1 + 1 = 2
             _____  2 + (len - left) -> 2 *
            
            2 + 4 = 6
        '''

        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans