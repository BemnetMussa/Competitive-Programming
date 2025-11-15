class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for ope in operations:
            if ope[1] == "+":
                x += 1
            else:
                x -= 1

        return x