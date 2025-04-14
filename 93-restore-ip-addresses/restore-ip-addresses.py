class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # Early exit if the string is too long to be a valid IP
        if len(s) > 12:
            return res

        def backtrack(i, dots, currIp):
            # If we have placed all 4 dots and reached the end of the string
            if dots == 4 and i == len(s):
                res.append(currIp[:-1])  # Remove the trailing dot
                return
      
            if dots > 4:
                return

            for j in range(i, min(i+3, len(s))):
                segment = s[i:j+1]
                if int(segment) <= 255 and (i == j or s[i] != "0"): 
                    backtrack(j+1, dots + 1, currIp + segment + ".")

        backtrack(0, 0, "")
        return res
