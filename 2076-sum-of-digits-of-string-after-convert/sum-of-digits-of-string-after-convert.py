class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ''
        # Convert
        for char in s:
            ans += str((ord(char) - ord('a') + 1))

        # transform 
        ans = self.transform(ans)
        k -= 1

        # transform k > 0
        while k > 0:
            ans = self.transform(ans)
            k -= 1

        return int(ans)


    def transform(self, ans):
        val = 0
        for num in ans:
            val += int(num)


        return str(val)


        