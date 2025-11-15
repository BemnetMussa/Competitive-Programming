class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # am given nums[int] and k: int 
        # requested to get the number of subarrays that there GCD is k right ok 

        # since a subarray is contigious
        n = len(nums)
        count = 0
        
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == k:
                    count += 1
                elif g < k:
                    break 
        
        return count    