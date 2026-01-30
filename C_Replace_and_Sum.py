# Optimized Replace and Sum
def max_replace_optimzed(n, q_count, a, b, queries):
    answer = []
    
    #take max of a[i] and b[i]
    max_a = [max(a[i], b[i]) for i in range(n)]
    #propagate max from right to left
    for i in range(n-2, -1, -1):
        max_a[i] = max(max_a[i], max_a[i+1])
    
    prefix_sum = [0] * n
    prefix_sum[0] = max_a[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + max_a[i]

    for left, right in queries:
        left -= 1  
        right -= 1
        total = prefix_sum[right] - (prefix_sum[left-1] if left > 0 else 0)
        answer.append(total)
    
    print(*answer) 


t = int(input())
for _ in range(t):
    n, q_count = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q_count)]
    max_replace_optimzed(n, q_count, a, b, queries)
