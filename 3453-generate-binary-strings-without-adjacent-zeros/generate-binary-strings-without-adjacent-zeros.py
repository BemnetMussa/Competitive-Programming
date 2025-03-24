class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        bits = ["1", "0"]
        def dfs(arr):
            if len(arr) == n:
                ans.append("".join(arr))
                return 


            for bit in bits:
                if arr and arr[-1] == "0" and bit == "0":
                    continue
          
                arr.append(bit)
                dfs(arr)
                arr.pop()
            

            return ans

        return dfs([])


