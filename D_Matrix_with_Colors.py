t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []

    pos_dict = [[] for _ in range(k+1)]
    for i, x in enumerate(a):
        pos_dict[x].append(i)

    for c in range(1, k+1):
        if not pos_dict[c]:
            ans.append(0)
        else:
            row_min = min(pos_dict[c])
            row_max = max(pos_dict[c])
            col_min = row_min  # symmetric in this problem
            col_max = row_max
            width = col_max - col_min + 1
            height = row_max - row_min + 1
            ans.append(width + height)
    
    print(*ans)
