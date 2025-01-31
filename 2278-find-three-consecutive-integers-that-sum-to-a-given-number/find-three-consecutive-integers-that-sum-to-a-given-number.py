class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        

        if num % 3 == 0:
            ans = num // 3
            return [ans-1, ans, ans + 1]

        
        return []