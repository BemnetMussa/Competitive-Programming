class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left = max_sum = curr_sum = 0
        seen = set()

        for right in range(len(nums)):
            curr_sum += nums[right]
            while nums[right] in seen:
                pop_num = nums[left]
                seen.remove(pop_num)
                curr_sum -= pop_num
                left += 1

            max_sum = max(max_sum, curr_sum)
            seen.add(nums[right])

        return max_sum