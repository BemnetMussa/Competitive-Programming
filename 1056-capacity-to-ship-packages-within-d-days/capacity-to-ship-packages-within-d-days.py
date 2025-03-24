class Solution:
    def calculate_day(self, mid: int, weights: List[int]) -> int:
        calculated_day = 1  
        counter = 0 

        for i in range(len(weights)):
            counter += weights[i]
            if counter > mid: 
                calculated_day += 1
                counter = weights[i]  

        return calculated_day

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right - left) // 2  

            if self.calculate_day(mid, weights) <= days:
                right = mid - 1  
            else:
                left = mid + 1 

        return left  
