class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        op = 0

        hashMap = defaultdict(int)

        for num in nums:
            diff = k - num

            if diff in hashMap:
                op += 1
                hashMap[diff] -= 1

                if hashMap[diff] == 0:
                    del hashMap[diff] 
            else:
                hashMap[num] += 1

        return op
        
