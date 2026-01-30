

n = int(input())
x, y = map(int, input().split())

white_diff = abs(1 - x) + abs(1 - y) # 3, 5 --> 
black_diff = abs(n - x) + abs(n - y)

if white_diff <= black_diff:
    print("White")
else:
    print("Black")