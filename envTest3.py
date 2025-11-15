y"""
- x XOR num1 is minimal
- x has the same number of bits as **nums2

X -> is uniquely determined
"""

count = bin(num2).count('1');
result = 0

for i in reversed(range(32)):
    if nums1 & (1 << i):
        if count > 0:
            result |= (1 << i)
            count -= 1

for i in range(32):
    if count == 0:
        break
    if not (result & ( 1 << i)):
        result |= (1 << i)
        count -= 1

return result
