class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:


        set_word = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            res = []
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in set_word:
                    for sub in dfs(end):
                        res.append(word + (" " + sub if sub else ""))

            memo[start] = res
            return res

        return dfs(0)

        


