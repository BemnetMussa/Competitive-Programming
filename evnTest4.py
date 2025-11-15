
count  = bin(nums2).count("1") # setbits
x = 0

for i in reversed(range(32)):
    if nums1 & (1 << j): # same as x
        if count > 0:
            x |= (1 << i)
            count -= 1

for i in range(32):
    if count == 0:
        break
    if not (x & ( 1 << i )):
        x |= (1 << i)
        count -= 1

return x
