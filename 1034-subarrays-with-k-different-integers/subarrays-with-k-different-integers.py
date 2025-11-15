class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums[] and integer k.
        return the Good subarray -> is a subarry that have exactly k unique integers

        *subarry is just sub array of an array which is contiguous.

        Approche -> sliding window by keeping track of 
                        - frequency of the integers
                        - subarries 

        nums = [1,2,1,2,3], k = 2
                ___                     [1, 2]
                _____                   [1, 2, 1], [2, 1]
                _______                 [1, 2, 1, 2], [2, 1, 2], [1, 2]
                _________   > k
                      ____  == k         [2, 3]

            [1,2,1,3,4]
             | | | |    -> [1, 2, 1, 3]
                 | | |  -> [1, 3, 4]
            --> a problem it counts the subarrys of not actual k 
             | |   -> [1, 2]
             | | | -> [1, 2, 1], [2, 1]
                 | | -> [1, 3]
                   | | -> [3, 4]
        
        Time Complexity O(n), space complexity O(n)
        Psuedocode
        freq = {}
        left = 0

        num_subarry = 0

        for right, num in enumerate(nums):
            freq[num] = freq.get((num, 0) + 1) **
            while len(freq) > k: # shrink the window 
                freq[left] -= 1
                left += 1

            num_subarry += right - left + 1 

        return num+subarry
        """
        def most(k):
            freq = {}
            left = 0

            num_subarry = 0

            for right, num in enumerate(nums):
                freq[num] = freq.get(num, 0) + 1
                while len(freq) > k: # shrink the window 
                
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                
            
                num_subarry += right - left +1

            return num_subarry

        return most(k) - most(k-1)