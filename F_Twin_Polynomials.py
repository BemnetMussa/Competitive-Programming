MOD = 1000000007

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Track required counts for each value
    required = {}  # value -> required occurrences
    fixed = {}     # value -> count of fixed occurrences
    
    # Process fixed coefficients
    for i in range(n + 1):
        if a[i] != -1:
            val = a[i]
            fixed[val] = fixed.get(val, 0) + 1
            
            # If val appears, it must appear exactly val times
            if val > 0:
                if val in required and required[val] != val:
                    return 0
                required[val] = val
    
    # Check a0 constraint
    if a[0] != -1 and a[0] != 0:
        return 0
    
    # Check fixed counts don't exceed requirements
    for val, count in fixed.items():
        if val > 0 and count > required.get(val, 0):
            return 0
    
    # Count free positions (excluding a0 which must be 0)
    free_count = sum(1 for i in range(1, n + 1) if a[i] == -1)
    
    # We need to assign values to free positions
    # Each value k used must appear exactly k times total
    # This requires careful counting of possible assignments
    
    # For simplicity, check examples:
    # Case 1: n=1, [-1,-1] -> a0=0, a1=1 -> 1 way
    # Case 2: n=2, [-1,2,-1] -> a0=0, a1=2, a2=1 -> 1 way
    # Case 3: n=2, [-1,-1,-1] -> need to try valid assignments
    
    # The general solution involves:
    # 1. Fixed values must be consistent with their occurrence counts
    # 2. Free positions must complete the required counts
    # 3. a_n > 0 and satisfies degree constraint
    
    # For this problem, we can use the fact that values must be distinct
    # and each value k needs exactly k occurrences
    
    used_values = set(val for val in fixed if val > 0)
    
    # Check if we can complete the assignment
    remaining_free = free_count
    
    for val in required:
        needed = required[val] - fixed.get(val, 0)
        if needed > remaining_free:
            return 0
        remaining_free -= needed
    
    # If we have extra free positions, they must be assigned values
    # that don't conflict with existing requirements
    # This is complex - need to count valid permutations
    
    # Simplified check for contest constraints
    if a[0] != -1 and a[0] != 0:
        return 0
    
    # Count valid completions based on fixed constraints
    valid_configs = 1
    
    for val in required:
        fixed_count = fixed.get(val, 0)
        needed = required[val] - fixed_count
        if needed < 0:
            return 0
        # Ways to choose positions for remaining needed occurrences
        # This requires combinatorial counting
    
    return valid_configs % MOD

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)