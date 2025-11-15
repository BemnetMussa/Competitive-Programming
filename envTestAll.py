
1514. Path with Maximum Probabilyt
"""
'''
Given: an undirected weighted graph of n nodes ( 0-indexed ). represented by an edge list where edges[i] = [a, b], succProb[i] is the prbabily of success

n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

REquested: max prbabily of success to go from start to end and return it's success probabily 
Approch: bfs approch on all nodes. keeping track of nodes
itearte through it. keep track of the probabilty hold on!
since there will be *start and *end what i created as a tree rather than keepign it graph
'''

# build graph with probabilties 
adj_list = defaultdict(list)
for (u, v), prob in zip(edges, succProb):
    adj_list[u].append((v, prob))
    adj_list[v].append((u, prob))

# Max-heap: (-probabilitey, node)
heap = [(-1.0, start)]
max_prob = [0.0] * n
max_prob[start] = 1.0

while heap:
    prob, node = heapq.heappop(heap)
    prob = -prob # convert to positive
    
    if node == end:
        return prob
    
    for neigh, neigh_prob in adj_list[node]:
        new_prob = prob * neigh_prob
        if new_prob > max_prob[neigh]:
            max_prob[neigh] = new_prob
            heap.heappush(heap, (-new_prob, neigh))

return 0.0


# 474. Ones and Zeroes
'''
# Given an array of binary strings *strs and two integer *m and *n.
Requested: to rutnr the largest subset x in y with at most m an -> 0's and n -> 1's

strs = ["10","0001","111001","1","0"], m = 5, n = 3
         
'''

max_leng = 0
for word in strs:
    counter = Counter(word)
    if counter['0'] <= m and counter['1'] <= n:
        max_leng = max(max_leng, len(word))

return max_leng # time -> O(n*m) and space O(1)

# 204. Count Primes
# given n 
# requetsed to find prime numbers that are less than n
# is it prime-or-not-prime
n = 10
if n < 2:
    print( 0)

def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0: # means there is antoher divisor of n 
            return False
        d += 1
    return True

count = 0
for i in range(2, n):
    if is_prime(i):
        count += 1
print(count)
# D. Flowers

MOD = 10**9 + 7
max_flowers = 10**5

t, k = map(int, input().split())
        
dp = [0] * (max_flowers + 1)
dp[0] = 1 # base case

for i in range(1, max_flowers + 1):
    dp[i] = dp[i-1]
    
    # last k flowers are white
    if i >= k:
        dp[i] = (dp[i] + dp[i-k]) % MOD


prefix_sum = [0] * (max_flowers+1)
prefix_sum[0] = dp[0]
for i in range(1, max_flowers+1)
    prefix_sum[i] = (prefix_sum[i-1] + dp[i]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    result = (prefix_sum[b] - prefix_sum[a-1] + MOD ) % MOD
    print(result)
"""


