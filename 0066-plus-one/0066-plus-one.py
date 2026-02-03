class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits) -1, -1, -1):
            digits[i] = digits[i] + carry 
            if digits[i] % 10 == -0 and digits[i] != 0:
                digits[i] = 0
                carry = 1
            else:
                carry = 0

        if carry:
            return [carry] + digits
        else:
            return digits
            