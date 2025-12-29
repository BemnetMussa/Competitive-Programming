class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        '''
        nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10
                    |                 | 
                                    --> unecessarly complex.
             -----------------------------
             

        going to be maintained.

        brute force approch will be: gropign it based on the increasing and decreasing form the pivot and also stroing how many is a dublicate values are there that is it 

        space O(n) + time O(n)
        '''
        max_nums_pivot = []
        min_nums_pivot = []
        same_pivot = 0

        for num in nums:
            if num == pivot:
                same_pivot += 1
            elif num < pivot:
                min_nums_pivot.append(num)
            else:
                max_nums_pivot.append(num)

        min_nums_pivot.extend([pivot for _ in range(same_pivot)])
        min_nums_pivot.extend(max_nums_pivot if max_nums_pivot else [])
        return min_nums_pivot

