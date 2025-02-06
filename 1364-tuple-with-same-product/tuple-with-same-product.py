class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        count = 0
        product_map = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]

                product_map[product] += 1

        for product in product_map.values():
            if product > 1:
                
                # in how many different ways a,b,c,d can be combined
                count += (product * (product - 1) // 2) * 8
        
        return count
