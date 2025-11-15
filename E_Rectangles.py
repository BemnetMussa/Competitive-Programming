import sys

class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [10**9] * (2 * self.size)
    
    def update(self, l, r, value):
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                self.data[l] = min(self.data[l], value)
                l += 1
            if r % 2 == 0:
                self.data[r] = min(self.data[r], value)
                r -= 1
            l //= 2
            r //= 2

    def query(self, index):
        res = 10**9
        i = index + self.size
        while i:
            res = min(res, self.data[i])
            i //= 2
        return res

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); m = int(data[index+1]); index += 2
        grid = []
        for i in range(n):
            grid.append(data[index]); index += 1

        ones = []
        for i in range(n):
            row_ones = []
            for j in range(m):
                if grid[i][j] == '1':
                    row_ones.append(j)
            ones.append(row_ones)
        
        row_lists = [[] for _ in range(n)]
        
        for u in range(n):
            list_u = ones[u]
            for d in range(u+1, n):
                list_d = ones[d]
                common = []
                i1, i2 = 0, 0
                while i1 < len(list_u) and i2 < len(list_d):
                    if list_u[i1] == list_d[i2]:
                        common.append(list_u[i1])
                        i1 += 1
                        i2 += 1
                    elif list_u[i1] < list_d[i2]:
                        i1 += 1
                    else:
                        i2 += 1
                if len(common) < 2:
                    continue
                min_col = common[0]
                max_col = common[-1]
                min_width = 10**9
                for i in range(1, len(common)):
                    width = common[i] - common[i-1] + 1
                    if width < min_width:
                        min_width = width
                A = (d - u + 1) * min_width
                for i in range(u, d+1):
                    row_lists[i].append( (min_col, max_col, A) )
                    
        seg = SegmentTree(m)
        ans_grid = [[0] * m for _ in range(n)]
        for i in range(n):
            seg.data = [10**9] * (2 * seg.size)
            for (l, r, A) in row_lists[i]:
                seg.update(l, r, A)
            for j in range(m):
                val = seg.query(j)
                if val == 10**9:
                    ans_grid[i][j] = 0
                else:
                    ans_grid[i][j] = val
                    
        for i in range(n):
            output_lines.append(" ".join(map(str, ans_grid[i])))
            
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()