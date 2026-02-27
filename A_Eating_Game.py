def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    zmax = max(a)
    print(a.count(zmax))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()