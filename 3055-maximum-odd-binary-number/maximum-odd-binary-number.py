class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        # counting the characters of 1
        # substracting the number of 1 from the length of s = num of zeros
        # taking -1 from the ones count for the last one : it works becase it is at least the string have 1 character of 1
        
        ones = s.count("1") 
        zeros = len(s) - ones

        ans = []
        for i in range(ones-1):
            ans.append("1")

        for i in range(zeros):
            ans.append("0")

        # the one that we have substracted such that it will be on the last 
        ans.append("1")

        return "".join(ans)
        



        