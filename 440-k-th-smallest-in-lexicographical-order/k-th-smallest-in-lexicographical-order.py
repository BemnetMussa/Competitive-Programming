class Solution(object):
    def helper(self, curr, n): # function returns the count of nodes of a curr subtree
        res = 0
        neig = curr + 1
        while curr <= n:
            res += min(neig, n + 1) - curr
            curr *= 10
            neig *= 10
        return res

    def findKthNumber(self, n, k):
        curr = 1
        k -= 1 
        while k > 0:
            steps = self.helper(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr
