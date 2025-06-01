class Solution(object):
    def distributeCandies(self, n, limit):
        res = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2 * limit:
                res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res