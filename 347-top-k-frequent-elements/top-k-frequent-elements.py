class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort Algorithm 

        # bucket size == len(nums) at max one element will have len(nums) repeating nums
        bucket = [[] for _ in range(len(nums)+1)]

        freq_counter = Counter(nums)
        for n, f in freq_counter.items():
            bucket[f].append(n)

        ans = []
        
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                ans.extend(bucket[i])
                if len(ans) == k:
                    return ans


        