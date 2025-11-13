# 3228. Maximum Number of Operatoins to Move Ones to the End
'''
choose an i, where i + 1 < len(s)
move the character s[i] to the ned of the string or upto 1

apporch:
Example: "1001101"
          0011101 -> 1 ---> stack = [1, 0], -> [0, 1]
          0011011 -. 1 ---> stack = [0, 0, 1]
          0010111 -> 3
          0001111 _. 4

'''

class Solution:
    def maxOperations(self, s: str) -> int:

        counted_ones = 0
        operations = 0
        
        for i,ch in enumerate(s):

            if ch =="1":
                counted_ones +=1

            else:
                if i ==0 or s[i-1] =="1":
                    operations += counted_ones
        
        return operations