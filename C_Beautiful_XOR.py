import sys

def query(q_type, left, right):
    print(f"{q_type} {left} {right}", flush=True)
    res = sys.stdin.readline().strip()
    if not res or res == '-1':
        sys.exit()
    return int(res)

def solve():
    n_str = sys.stdin.readline()
    if not n_str:
        return
    n = int(n_str)

    sum_p_total = query(1, 1, n)
    sum_a_total = query(2, 1, n)
    k = sum_a_total - sum_p_total

    l, low, high = -1, 1, n
    while low <= high:
        mid = (low + high) // 2
        diff = query(2, 1, mid) - query(1, 1, mid)
        if diff == 0:
            low = mid + 1
        else:
            l = mid
            high = mid - 1

    print(f"! {l} {l + k - 1}", flush=True)

def main():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    for _ in range(int(t_str)):
        solve()

if __name__ == "__main__":
    main()
