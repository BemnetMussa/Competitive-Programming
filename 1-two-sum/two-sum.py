class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
            
        
        '''

        d_track = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in d_track:
                return [d_track[diff], index]
            d_track[value] = index

        return []