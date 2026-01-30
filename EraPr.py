### Action File
# Contest 1 ---- Div 3
# A. DBMB and the Array
"""
def check_(array, s, x):
    total = sum(array)

    if total > s:
        return print("No") 

    reminder_ = s - total 
    if reminder_ % x == 0:
        return print("Yes")

    return print("No")
    
test_cases = int(input())
for i in range(test_cases):
    n, s, x = map(int, input().split())
    array = list(map(int, input().split()))
    
    check_(array, s, x)


# B. Reverse a Permutation 
def lexicographically_max(n, array):

    valid_i = n
    for current_i, current_value in enumerate(array):
        if current_value != valid_i:
            # find the correct place
            for search_i in range(current_i, n):
                if array[search_i] == valid_i:
                    # reverse operation
                    array[current_i:search_i+1] = array[current_i:search_i+1][::-1]
                    print(*array)
                    return 

        valid_i -= 1

    print(*array)

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    lexicographically_max(n, array)

# C. Replace and Sum 
def max_replace(n, q, a, b, q):
    original = a.copy()
    answer = []

    for left, right in q:
        total = 0

        for i in range(left, right + 1):
            if a[i] < b[i]:
                total += b[i]
                a[i] = b[i]
            elif i + 1 < n and a[i] < a[i+1]:
                total += a[i+1]
                a[i], a[i+1] = a[i+1], a[i]
            else:
                total += a[i]
        a = original_a.copy()
        answer.append(total)

    print(*answer)
"""
t = int(input())
for _ in range(t):
    n, q_count = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q_count)]
    max_replace_optimzed(n, q_count, a, b, queries)

# Time complexity O(n*q) -- which will not pass
# optimizatino -- prefixsum
def max_replace_optimzed(n, q_count, a, b, queries):
    answer = []
    max_a = [max(a[i], b[i]) for i in range(n)]
    # propagate the max from teh right to left
    for i in range(n-2, -1, -1):
        max_a[i] = max(max_a[i], max_a[i+1])

    # Build prefix sums
    prefix_sum = [0] * n
    prefix_sum[0] = max_a[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + max_a[i]

    for left, right in queries:
        left -= 1
        right -= 1
        total = prefix_sum[right] - (prefix_sum[left-1] if left > 0 else 0)

        answer.append(total)
    print(answer)

        
