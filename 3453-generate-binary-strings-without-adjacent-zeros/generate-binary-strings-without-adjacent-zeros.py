class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        def backtrack(curr):
            if len(curr) == n:
                ans.append(curr)
                return 
        
            backtrack(curr + "1")
            if not curr or curr[-1] == "1":
                backtrack(curr + "0")

        backtrack("")
        return ans
