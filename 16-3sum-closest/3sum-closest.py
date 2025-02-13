class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest_sum = float("inf")


        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1


            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]

                if abs(target-sum_) < abs(target-closest_sum):

                    closest_sum = sum_

                if sum_ > target:
                    right -= 1
                
                elif sum_ < target:
                    left += 1
                else:
                    return target

        
        return closest_sum