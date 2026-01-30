class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        '''
        Given an array of prices
        return the number of smooth descent periods 

        approch:
        prices = [3, 2, 1, 4]
                  _             -> 1
                  ____          -> 1 + 1
                  _______       -> 1 + 2
                           _    -> 1
                                    total = 7 correct
                [3], [2], [1], [4], [3, 2], [2, 1], [3, 2, 1]
        '''

        count = 0 # 1 + 1 + 1 + 1 + 2 + 1 
        left = 0

        for right, num in enumerate(prices):
            count += 1 # as a single number
            if right > 0 and prices[right-1] - prices[right] == 1:
                count += (right - left)

            else:
                left = right
            print(num, count)

        
        return count 
