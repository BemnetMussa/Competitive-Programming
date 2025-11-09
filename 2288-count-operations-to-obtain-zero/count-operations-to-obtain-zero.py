class Solution:
    def countOperations(self, nums1: int, nums2: int) -> int:
        
        op = 0
        while nums1 != 0 and nums2 != 0:
            if nums1 >= nums2:
                nums1 = nums1 - nums2
            else:
                nums2 = nums2 - nums1
            op += 1

        return op