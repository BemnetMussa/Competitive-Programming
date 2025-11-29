
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not (k%2 and k%5):
            return -1

        # rem = 1
        # count = 1
        n = 1
        for i in range(1, k+1):
            if n % k == 0:
                return i
            n = n*10 + 1
        return i
        

        # while rem%k:
        #     N = rem *10 + 1
        #     rem = N%k
        #     count += 1
        #     print(N, rem,count)
            
        
        # # return count