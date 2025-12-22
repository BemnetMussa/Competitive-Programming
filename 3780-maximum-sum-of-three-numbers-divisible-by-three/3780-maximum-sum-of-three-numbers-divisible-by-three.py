class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Reminder of 3 always will be inside [0, 1, 2]
        r0, r1, r2 = [], [], []
        nums.sort(reverse=True)

        for num in nums:
            if num % 3 == 0:
                r0.append(num)
            elif num % 3 == 1:
                r1.append(num)
            else:
                r2.append(num)
        
        ans = 0
        if len(r0) >= 3: # case0: 0 + 0 + 0
            ans = max(ans, r0[0] + r0[1] + r0[2])
        if len(r1) >= 3: # case1: 1 + 1+ 1
            ans = max(ans, r1[0] + r1[1] + r1[2])
        if len(r2) >= 3: # case2: 2 + 2 + 2
            ans = max(ans, r2[0] + r2[1] + r2[2])
        # case3: 0 + 1 + 2
        if len(r0) >= 1 and len(r1) >= 1 and len(r2) >= 1:
            ans = max(ans, r0[0] + r1[0] + r2[0])

        return ans # time complexity O(nlogn) and space of O(n)
        
        