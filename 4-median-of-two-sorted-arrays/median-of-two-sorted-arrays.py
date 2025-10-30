class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 2000
        # sorign and return the mid if it is odd other wise even plus and return the half
        '''
        nums1 = [1, 3], nums2 = [2]
                   2             1 = 3 // 2 = 1 idx

                 |  | 
        
        merge sort:
        [1, 3] [2]
             |  |    -> [1, 2 ,3]
     sorted_array = [1, 2, 3] -> find the mid with respec tof *(even) and *(odd)
        Logn
        
        '''

        sorted_array = []
        ptr = ptr1 = 0

        while ptr < len(nums1) and ptr1 <len(nums2):
            if nums1[ptr] < nums2[ptr1]:
                sorted_array.append(nums1[ptr])
                ptr += 1
            else:
                sorted_array.append(nums2[ptr1])
                ptr1 += 1

        if ptr < len(nums1):
            sorted_array.extend(nums1[ptr:])

        if ptr1 < len(nums2):
            sorted_array.extend(nums2[ptr1:])
        # complete sorted_array since we just comapring values 
        
        n = len(sorted_array)
        mid = n // 2

        if n % 2 == 0: # even length
            return (sorted_array[mid-1] + sorted_array[mid]) / 2
        else: # odd length
            return float(sorted_array[n//2])