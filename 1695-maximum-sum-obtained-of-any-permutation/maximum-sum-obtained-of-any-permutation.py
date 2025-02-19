class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        nums.sort(reverse=True)


        freq = [0] * len(nums)
         
        # Fill in the frequency for each index in the requests
        for start, end in requests:
            freq[start] += 1
            if end + 1 < len(nums):
                freq[end + 1] -= 1


        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        # Sort the frequency in descending order to match with sorted nums
        freq.sort(reverse=True)

        result = sum(nums[i] * freq[i] for i in range(len(nums)))
   
        return result % (10**9 + 7)
