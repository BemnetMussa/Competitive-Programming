'''
given an array[int] 
requested to return  [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

approch:
brute force approch
for i in nums:
    for j in (i+1, nums):
        for k in (j + 1, nums):
            if nums[i] + nums[j] + nums[k] == 0
                res.append([i, j, k])

O(n^3)

nums = [-1,0,1,2,-1,-4]          hashmap key: value , where key= value, value = index
         | |            -1 + (?) = 0 -> is there is 1 in my hashmap? if there is then take the index and delete it. since no duplicate triplests are allowed 

O(n^2)


'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # pass duplicates


            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total > 0:
                    right -= 1
                else: 
                    left += 1


        return res

            

