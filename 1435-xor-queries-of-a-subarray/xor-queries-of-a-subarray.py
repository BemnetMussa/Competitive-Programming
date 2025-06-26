class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # it is just prefix xor simply
        n = len(arr)

        prefix_xor = [0] * (n + 1)

        for i in range(1, n+1):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i - 1]

        ans = []
        for left, right in queries:
            result = prefix_xor[right+1] ^ prefix_xor[left]

            ans.append(result)

        return ans