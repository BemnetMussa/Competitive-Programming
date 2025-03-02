class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # for tracking the reminders
        mod_dict = {0: -1}

        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            rem = curr_sum % k

            if rem not in mod_dict:
                mod_dict[rem] = i

            elif i - mod_dict[rem] > 1:
                return True

        return False
