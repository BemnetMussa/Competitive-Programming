class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                pair = [i, j]
       
          
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    if pair not in pairs:
                        pairs.append(pair)
  
        return len(pairs)