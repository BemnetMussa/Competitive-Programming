class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        


        nums_counter = Counter(nums)

        pair = 0
        non_pair = 0
        
        for value in nums_counter.values():
            
            if value % 2 == 0:
                pair += (value // 2)

            else:
                pair += (value // 2)
                non_pair += (value % 2)

        
        return [pair, non_pair]


