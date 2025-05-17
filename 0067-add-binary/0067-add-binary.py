class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result = []
        carry = 0

        # Start from the rightmost bit
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            sum_val = carry
            if i >= 0:
                sum_val += int(a[i])  # Extract the bit from a
                i -= 1
            if j >= 0:
                sum_val += int(b[j])  # Extract the bit from b
                j -= 1

            # Append the computed binary digit
            result.append(str(sum_val % 2))

            carry = sum_val // 2

        
        return ''.join(result[::-1])

