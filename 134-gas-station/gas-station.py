'''
Given : gas tanks in ciercular route and the amount of it is gas[i], 
        cost to travel from one gas startion to another is cost[i]

Requested: return the idx to start on that will allow us to return back in circule.
Solution: 
- gas = [1,2,3,4,5], cost = [3,4,5,1,2]
         1,2,3,4,5,1,2,3,4,5
         3,4,5,1,2,3,4,5,1,2
             |         |      --> O(n^2) 

  (gas, cost)
  [(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)]
    gas-cost
  [(-2), [-2], [-2], [3], [3]]
   
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0 

        
        return start if total_tank >= 0 else -1