import sys
import bisect

def solve():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    b.sort() 
    min_prev_val = float('-inf')

    for i in range(n):
        current_min_val = float('inf')  
        # Option 1: Keep a[i] as is
        if a[i] >= min_prev_val:
            current_min_val = min(current_min_val, a[i])

        # Option 2: Transform a[i] to b[j] - a[i]
        # We need b[j] - a[i] >= min_prev_val
        # This implies b[j] >= min_prev_val + a[i]
        target_b_val = min_prev_val + a[i]

        # Find the first b[j] that is >= target_b_val using binary search
        idx = bisect.bisect_left(b, target_b_val)
        if idx < m:
            transformed_val = b[idx] - a[i]
            current_min_val = min(current_min_val, transformed_val)

        if current_min_val == float('inf'):
            print("NO")
            return
        
        min_prev_val = current_min_val

    print("YES")

def main():
    sys.stdin = open(0)  # To ensure fast input handling
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
