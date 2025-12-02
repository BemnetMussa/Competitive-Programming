
n = int(input())
matrix = []
for _ in range(n):
    li = list(map(int, input().split()))
    matrix.append(li)

good_sum = 0
# main diagonal 
for i in range(n):
    good_sum += matrix[i][i]

# secondary diagonal
for i in range(n):
    
    good_sum += matrix[i][n-(i+1)]

# middle column & middle row
mid = (n-1)//2

for i in range(n):
    good_sum += matrix[i][mid]
    good_sum += matrix[mid][i]

print(good_sum - (matrix[mid][mid] * 3))
    