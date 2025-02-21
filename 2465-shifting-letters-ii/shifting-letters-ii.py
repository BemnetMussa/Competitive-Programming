class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        f = [0] * (len(s) + 1)  

        for start, end, sign in shifts:
            if sign == 1:
                f[start] += 1
                if end + 1 < len(f): 
                    f[end + 1] -= 1
            else:
                f[start] -= 1
                if end + 1 < len(f):
                    f[end + 1] += 1
        
        
        diff = 0
        res = [ord(c) - ord("a") for c in s]

        for i in range(len(f[:-1])):
            diff += f[i]
            res[i] = (diff + res[i]) % 26

        s = [chr(ord("a") + n) for n in res]
        return "".join(s)

