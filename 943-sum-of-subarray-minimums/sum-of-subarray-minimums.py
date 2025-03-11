class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = []
        arr.append(float("-inf"))

        for i in range(len(arr)):

            while stack and arr[i] < arr[stack[-1]]:
                left = stack.pop()
                right = i - 1
                prev_index = stack[-1] if stack else -1
                res += (left - prev_index) * (right - left + 1) * arr[left]
            
            stack.append(i)

        return res % MOD
