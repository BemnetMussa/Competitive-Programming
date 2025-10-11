class Solution:
    def findGCD(self, nums: List[int]) -> int:
        zmin = min(nums)
        zmax = max(nums)

        return math.gcd(zmin, zmax)