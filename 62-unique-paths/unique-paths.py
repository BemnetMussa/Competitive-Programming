class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Given a M * N , Grid[int][int] and a robot located at top-left corner and want to reach bottom right corner. 
            - only move allowed Down or Right
        Request: to get every possible unqie paths that the robot can take.

        constraint: 1 <= m, n <= 100

        Approche: 
        - since it is requested to get every single uinque path. we need to consider every path
        - for this approche the brute force approche will be iterating through each one of the paths and tracking if the final path is unique then counting it for every single path starting from the first 
        - better soltion interms of time will be DP

        state; i, j
        base_case: reaching bttom right corner & out of bound
        recursive relation: dp(i, j)

        psuddocode:
        funciton dp(i, j):
            if i > M - 1 or j > N-1:
                return 0
            
            if (i, j) == (M-1, N-1):
                return 1
            
            return dp(i+1, j) + dp(i, j+1) #since each path will be unique why don't just couning it until it reaches the end 
        '''
        memo = {}
        def dp(i, j):
            if i > m-1 or j > n-1:
                return 0
            if (i, j) == (m-1, n-1):
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] =  dp(i+1, j) + dp(i, j+1)
            return memo[(i, j)]
        
        return dp(0, 0)