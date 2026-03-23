for _ in range(int(input().strip())):
    n = input()
    
    zeros = n.count("0")
    onces = n.count("1")

    if min(zeros, onces) % 2 == 0:
        print("NET")
    else:
        print("DA")