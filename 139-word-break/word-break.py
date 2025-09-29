class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)

        @lru_cache(None)
        def dp(idx):
            # base case
            if idx >= N:
                return True
            
            for j in range(idx+1, len(s)+1):
                if s[idx:j] in wordDict and dp(j):
                    return True

            return False

        return dp(0)

            