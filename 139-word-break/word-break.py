class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        memo = {}
        def dp(idx):
            # base case
            if idx >= N:
                return True
            
            if idx in memo:
                return memo[idx]

            for j in range(idx+1, len(s)+1):
                if s[idx:j] in wordDict and dp(j):
                    memo[idx] = True
                    return memo[idx]

            memo[idx] = False
            return memo[idx]

        return dp(0)

            