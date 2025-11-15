n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def max_dist2(x):  # returns squared distance
    return max((xi - x)**2 + (yi - x)**2 for xi, yi in points)

left, right = -1e7, 1e7
for _ in range(100):  # fixed number of iterations is enough
    m1 = left + (right - left) / 3
    m2 = right - (right - left) / 3
    d1 = max_dist2(m1)
    d2 = max_dist2(m2)
    if d1 > d2:
        left = m1
    else:
        right = m2

best = max_dist2((left + right) / 2)**0.5  # take sqrt at the end
print(f"{best:.6f}")
