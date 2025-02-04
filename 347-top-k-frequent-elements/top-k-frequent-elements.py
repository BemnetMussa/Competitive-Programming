class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_s = Counter(nums)
    
        sorted_dict = dict(sorted(count_s.items(), key=lambda x: x[1], reverse=True))

        ans = []

        for num in sorted_dict.keys():
            if len(ans) < k:
                ans.append(num)

        return ans