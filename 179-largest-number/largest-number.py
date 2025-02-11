from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):

        nums = list(map(str, nums))
    
        def compare(x, y):
            # return -1 to put x before y
            if x + y > y + x:
                return -1  
            # return 1 to put y before x
            elif x + y < y + x:
                return 1 
            # no change it will be placed in order
            else:
                return 0 

        print(nums)

        nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums)

        if result[0] == '0':
            return '0'
        
        return result
