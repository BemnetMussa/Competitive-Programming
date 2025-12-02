ROWS, COLS = map(int, input().split())
matrix = [list(input()) for _ in range(ROWS)]

possible = True

directions = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == 'W':
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < ROWS and 0 <= nj < COLS:
                    if matrix[ni][nj] == 'S':  
                        possible = False
                        break
        if not possible:
            break
    if not possible:
        break

if not possible:
    print("No")
else:
    print("Yes")
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == '.':
                matrix[i][j] = 'D'
    for row in matrix:
        print("".join(row))
