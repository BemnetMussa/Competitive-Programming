class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        

        ans = [0] * len(s)


        for index, val in enumerate(indices):

            ans[val] = s[index]

        return "".join(ans)