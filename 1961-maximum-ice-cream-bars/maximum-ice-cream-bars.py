class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)


        for cost in costs:
            count[cost] += 1

        ice = 0

        for price in range(1, max_cost + 1):
            if count[price] > 0:  

                num_to_buy = min(count[price], coins // price)
                ice += num_to_buy
                coins -= num_to_buy * price

                if coins == 0:
                    break

        return ice
