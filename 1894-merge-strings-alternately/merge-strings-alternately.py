class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        for i in range(max(n, m)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i]) # this was not cool damnn how did i didn't think about it
        return "".join(res)
