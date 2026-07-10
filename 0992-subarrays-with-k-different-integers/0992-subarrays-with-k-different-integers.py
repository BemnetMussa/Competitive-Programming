class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def solve(k):
            window = defaultdict(int)
            l = 0
            ans = 0

            for r in range(len(nums)):
                window[nums[r]] += 1

                while len(window) > k:
                    window[nums[l]] -= 1
                    if window[nums[l]] == 0:
                        del window[nums[l]]
                    l += 1

                ans += r - l + 1

            return ans

        return solve(k) - solve(k-1)
        # nums = [1,2,1,2,3], k = 2
        #         ___   -> [1, 2]
        #         _____ -> [1, 2, 1]
        #         _______ -> [1, 2, 1, 2]
        #         _________  -> [X]
        #               ____ -> [2, 3]

        # 1, 2, 1, 2, 3 = 5 , 4 - 5 = 1
        #12 - 5 = 7
