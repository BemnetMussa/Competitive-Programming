

# brute force approch 
# generate upto 1 upto 1000

prefix = ""
for i in range(1, 1000+1):
    prefix += str(i)

n = int(input())
print(prefix[n-1])

# for sake of effiency 
# same time and space so..