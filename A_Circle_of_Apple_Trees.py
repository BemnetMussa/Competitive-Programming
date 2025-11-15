import sys
import bisect

def solve():
    n = int(sys.stdin.readline())
    beauties = list(map(int, sys.stdin.readline().split()))

    beauties.sort()
    tails = []

    for beauty in beauties:
        idx = bisect.bisect_left(tails, beauty)
        if idx == len(tails):
            tails.append(beauty)
        else:
            tails[idx] = beauty

    print(len(tails))

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
