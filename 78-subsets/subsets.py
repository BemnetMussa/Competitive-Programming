class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        temp = []
        def backtrack(subsets,idx):
            if idx==len(nums):
                temp.append(subsets[:])
                return
            
            #Take
            subsets.append(nums[idx])
            backtrack(subsets,idx+1)

            #don't take
            subsets.pop()
            backtrack(subsets, idx+1)

        backtrack([], 0)
        return temp