class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.minUnfairness = float("inf")

        def backtrack(i, max_so_far):
            if max_so_far >= self.minUnfairness:
                return
            if i >= len(cookies):
                self.minUnfairness = min(self.minUnfairness, max_so_far)
                return

            for j in range(k):
                child[j] += cookies[i]
                backtrack(i+1, max(max_so_far, child[j]))
                child[j] -= cookies[i]

                if child[j] == 0:
                    break

        
        backtrack(0, 0)

        return self.minUnfairness