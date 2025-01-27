class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        # Initialize the result array with 1s
        result = [1] * n

        # Compute prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

 
        # Compute suffix products and multiply with prefix values in result
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
     
        print(result)
        
        return result