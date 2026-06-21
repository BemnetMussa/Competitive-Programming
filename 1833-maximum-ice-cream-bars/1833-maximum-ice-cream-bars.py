class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxCost = max(costs)
        priceFrequency = [0] * (maxCost + 1)

        for coin in costs:
            priceFrequency[coin] += 1

        iceCreams = 0

        for cost in range(1, maxCost + 1):
            if coins > 0:
                toBuy = min(priceFrequency[cost], coins // cost)
                coins -= (toBuy * cost)
                iceCreams += toBuy
            else:
                break

        return iceCreams