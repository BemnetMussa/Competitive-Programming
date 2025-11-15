"""
Question:
- 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
- quesions must be in-order starting from question 0
- Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions.

Constraints:
-   1 <= questions.length <= 105
    questions[i].length == 2
    1 <= pointsi, brainpoweri <= 105

Requested: 
- Return the maximum points you can earn from the exam.

Approche:
- questions = [[3,2],[4,3],[4,4],[2,5]]     ans = 7
                
                
"""



class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)

        # Top-Down approch
        # memo = {}
        # def dp(idx):
        #     if idx >= N:
        #         return 0
        #     if idx in memo:
        #         return memo[idx]

        #     # solve current question 
        #     profit = questions[idx][0] + dp(idx + questions[idx][1] + 1)

        #     # skip current question
        #     skip = dp(idx + 1)
 
        #     memo[idx] = max(profit, skip)
        #     return memo[idx]

        # return dp(0)


        # Bottom-Down approch 
        N = len(questions)
        dp = [0] * (N + 1)  # Extra space to handle out-of-bound skips

        for i in range(N - 1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + brainpower + 1
            
            solve = points + (dp[next_q] if next_q < N else 0)
            skip = dp[i + 1]

            dp[i] = max(solve, skip) 

        return dp[0]