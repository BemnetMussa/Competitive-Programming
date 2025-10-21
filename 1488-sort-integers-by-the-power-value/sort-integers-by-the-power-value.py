class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        # lo, hi, k
        # [12, 13, 14, 15]
        # [9, 9,  17, 17] --> power for [lo, hi]
        def helper(val):
            steps = 0 # 2...
           
            while val != 1: # 12, 6, 3, 10, 5, ....
                if val % 2 == 0:
                    val /= 2
                else:
                    val = 3 * val + 1
                    
                steps += 1
                
            return steps
                    
        
        # sorting based on the power values, return k->index
        
        array = [x for x in range(lo, hi+1)]
     
        # sorting
        sorted_hash = {} # keys: steps, values: array[values]
        
        for i in range(len(array)):
            steps = helper(array[i]) # 12
            sorted_hash[array[i]] = steps
            
        sorted_array = []
        for key, value in sorted_hash.items():
            sorted_array.append((value, key))
        
        sorted_array.sort()
        
        return sorted_array[k-1][1]
            
        
            
        
        