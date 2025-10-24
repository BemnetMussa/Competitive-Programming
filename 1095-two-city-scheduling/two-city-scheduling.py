'''
costs = [[10,20],[30,200],[400,50],[30,20]]
Requested: to return the minijmum cost to fly eveyr person to a city such that exactly n people arraive in each city.

[[10,20],[30,200],[400,50],[30,20]]
  | 
  
'''



class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        # sort them based on the difference
        costs.sort(key=lambda x: x[1] - x[0]) # respect of b - a
        n = len(costs) // 2
        total = 0

        for i in range(n):
            total += costs[i][1] 

        for i in range(n, n*2):
            total += costs[i][0]

        return total