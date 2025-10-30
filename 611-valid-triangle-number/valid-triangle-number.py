class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # sorting the list
        # chekcign if a + b > c which means we can form a traingel out of it 
        # [1, 2, 3]
        #  |  

        nums.sort()
        count = 0

        for k in range(len(nums)-1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1

                else:
                    i += 1

            

        return count