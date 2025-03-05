class Solution:
   def minMoves(self, target: int, maxDoubles: int) -> int:
       moves = 0

       while maxDoubles > 0 and target > 1:
           if target % 2 == 1:
               target -= 1
           else:
               target //= 2
               maxDoubles -= 1
           moves += 1

       moves += target - 1
       
       return moves