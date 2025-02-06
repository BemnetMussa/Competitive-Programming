class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        

        even_sum = self.sumEven(nums)
           
        ans = []
        
        for q in queries:
            val, index = q
            
            # substracting from the even_sum if even
            # even_sum: 8   nums[index] = 2
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
                # even_sum= 6
            
            
            nums[index] = nums[index] + val
            #nums[index] = -1

            if nums[index] % 2 == 0:
                even_sum += nums[index]

            # [8, 6]
            ans.append(even_sum)

        return ans

    def sumEven(self, nums):
  
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        return even_sum
