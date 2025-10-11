
for _ in range(int(input())):

    n = int(input())
    cypher = list(map(int, input().split()))

    moves = []
    for _ in range(n):
        _, m = input().split()
        val = 0
        for char in m:
            if char == "D":
                val -= 1
            else:
                val += 1

        moves.append(val)
  
    ans = []
    zmask = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(n):
        ex = cypher[i] - moves[i]

        ans.append(zmask[ex % len(zmask)] )

    print(*ans)

