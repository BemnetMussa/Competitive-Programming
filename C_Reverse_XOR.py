def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n == 0:
            print("YES")
            continue
        
        # Get binary representation without '0b'
        bits = bin(n)[2:]
        length = len(bits)
        
        # Check if n is symmetric (palindromic) in binary
        is_palindromic = all(bits[i] == bits[length-1-i] for i in range(length//2))
        
        if is_palindromic:
            print("YES")
        else:
            print("NO")

solve()