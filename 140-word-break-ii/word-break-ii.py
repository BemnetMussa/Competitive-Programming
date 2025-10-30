class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #  s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
        #          |           -> len(cats) > | then it shoudln't be there
        #       ___             -> cat
        #       ____            -> 'cat', 'cats'
        #       _____           -> catsa -> not in dictionary
        #        ___-
        #    ....
        #          ____          -> 'cat sand', 'cats'  --> shoudl track of the pointer
        # [['cats', 'and'], [']

        # ----------- invalid too much confussion
        # catsanddog
        # cat sanddog
        # thinking about to use tire node fo rthe wordDict but the problem that i am facing is i can get the cat and cats and store them somewhere but the problem is how do i know where to put sand shoudl i put it on both no it is not the case what about and you see which i didn't solve the. so the problem is where to put it. and kep track of what to put hmmmmwhy do i keep track of it at the money when i increase the ptr morphhhhh. 
        # hmmm the recent one what why not dp hmmm the fuck


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

        


