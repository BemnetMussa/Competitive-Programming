class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        #  A= [1,3,2,4]  B= [3,1,2,4]
        #      | | |           
        #      |             |     [1]  in [3]   C[0] = 0
        #        |             |   [1, 3] in [3, 1]  c[1] = 2
        #   

        # res = []
        # while ( r < len(A)):
        #     currA = Counter(A[:r])
        #     currB = Counter(B[:r])

        #     if 

        n = len(A)
        ans = []
        seen = [0] * (n + 1)
        common = 0
        
        for i in range(n):
            if seen[A[i]] == 0:
                seen[A[i]] = 1
            elif seen[A[i]] == 1:
                common += 1
            if seen[B[i]] == 0:
                seen[B[i]] = 1
            elif seen[B[i]] == 1:
                common += 1
            ans.append(common)
        return ans