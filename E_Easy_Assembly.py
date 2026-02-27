n = int(input().strip())
towers = []
all_blocks = []

for _ in range(n):
    data = list(map(int, input().split()))
    blocks = data[1:]
    towers.append(blocks)
    all_blocks.extend(blocks)

sorted_blocks = sorted(all_blocks)
pos = { val: i for i, val in enumerate(sorted_blocks)}

splits = 0
for tower in towers:
    for i in range(len(tower)-1):
        if pos[tower[i]] + 1 != pos[tower[i+1]]:
            splits += 1

combines = (n + splits) - 1

print(splits, combines) # time complexity: O(KlogK), space complexity: O(K)