class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join(str(x) for x in digits))

        num += 1

        return [int(x) for x in str(num)]