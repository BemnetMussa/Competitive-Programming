class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charFrequency = Counter(text)
        count = 0

        flag = False
        while True:
            for c in "balloon":
                if c not in charFrequency.keys():
                    flag = True

                charFrequency[c] -= 1
                if charFrequency[c] == 0:
                    del charFrequency[c]

            if flag:
                break
            count += 1

        return count
            