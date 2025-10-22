class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        **Do not return anything, modify nums1 in-place instead.

        GIVEN:  nums1, nums2 with a length of m and n respectively. 
                len(nums1) is m + n where n elements in nums1 are 0
                sored in increasing order

        Requested: return concatenating nums1 and nums2 into sorted array.
                    modify the nums1. 

        constraints: 0 <= m, n <= 200, 1 <= m+n <= 200

        approch: 
            nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
                     _____ | | |
                     [1,2,3,2,5,6]
                     Then sort      # the soltuion -> O(n) 
        """


        i = m
        j = 0
        while i < (m + n):
            nums1[i] = nums2[j]
            i += 1
            j += 1

        nums1.sort()
