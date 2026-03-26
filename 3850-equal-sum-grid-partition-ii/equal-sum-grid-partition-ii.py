class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

   
        # Vertical cuts
        rightCounter = Counter()
        for r in range(R):
            for c in range(C):
                rightCounter[grid[r][c]] += 1

        leftCounter = Counter()
        leftSum = 0

        for cut in range(C - 1):
            # move column cut from right -> left
            colSum = 0
            for r in range(R):
                val = grid[r][cut]
                colSum += val
                leftCounter[val] += 1
                rightCounter[val] -= 1
                if rightCounter[val] == 0:
                    del rightCounter[val]

            leftSum += colSum
            rightSum = total - leftSum

            if leftSum == rightSum:
                return True

            diff = abs(leftSum - rightSum)

            # heavier side must contain diff
            if leftSum > rightSum:
                if diff in leftCounter:
                    # connectivity check if left part is 1D
                    if R == 1:
                        if grid[0][0] == diff or grid[0][cut] == diff:
                            return True
                    elif cut + 1 == 1:  # left width == 1
                        if grid[0][0] == diff or grid[R-1][0] == diff:
                            return True
                    else:
                        return True
            else:
                if diff in rightCounter:
                    # connectivity check if right part is 1D
                    if R == 1:
                        if grid[0][cut+1] == diff or grid[0][C-1] == diff:
                            return True
                    elif C - (cut + 1) == 1:  # right width == 1
                        if grid[0][cut+1] == diff or grid[R-1][cut+1] == diff:
                            return True
                    else:
                        return True

        # Horizontal cuts
        downCounter = Counter()
        for r in range(R):
            for c in range(C):
                downCounter[grid[r][c]] += 1

        upCounter = Counter()
        upSum = 0

        for cut in range(R - 1):
            rowSum = 0
            for c in range(C):
                val = grid[cut][c]
                rowSum += val
                upCounter[val] += 1
                downCounter[val] -= 1
                if downCounter[val] == 0:
                    del downCounter[val]

            upSum += rowSum
            downSum = total - upSum

            if upSum == downSum:
                return True

            diff = abs(upSum - downSum)

            if upSum > downSum:
                if diff in upCounter:
                    if C == 1:
                        if grid[0][0] == diff or grid[cut][0] == diff:
                            return True
                    elif cut + 1 == 1:  # up height == 1
                        if grid[0][0] == diff or grid[0][C-1] == diff:
                            return True
                    else:
                        return True
            else:
                if diff in downCounter:
                    if C == 1:
                        if grid[cut+1][0] == diff or grid[R-1][0] == diff:
                            return True
                    elif R - (cut + 1) == 1:  # down height == 1
                        if grid[cut+1][0] == diff or grid[cut+1][C-1] == diff:
                            return True
                    else:
                        return True

        return False