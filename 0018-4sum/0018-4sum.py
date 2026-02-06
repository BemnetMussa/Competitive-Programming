class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) -3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                left = j + 1
                right = len(nums) -1 

                while (left < right):
                    val = nums[i] + nums[j] + nums[left] + nums[right]

                    if val == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[left] == nums[right-1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif val < target:
                        left += 1

                    else:
                        right -= 1

        return res



