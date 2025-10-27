'''
Given: change from roman integer. 
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"LVIII"
 |     -> 50 + 5 + 3 = 58

"MCMXCIV"
 |     -> 1000 
  |    -> 1000 + 100
   |   _> 1000 + (100 < 1000 = substract prev with curr) 900
    |  -> 1000 + 900 + 10
     | -> 1000 + 900 + (X < c) = 90
      | -> 1000 + 900 + 90 + 1
       | -> 1000 + 900 + 90 + (I < V) = 4

1000 + 900 + 90 + 4 = 1994

needs:
 - dictionary holds the key: value -> roman symbols
 - iterating through it and checking 
 - stack

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        stack = [] # answer 

        for char in s:
            val = dictionary[char]
            if stack and stack[-1] < val:
                prev_val = stack.pop()
                val = val - prev_val

            stack.append(val)

        return sum(stack) # Time: O(N) and Space: O(N)


        