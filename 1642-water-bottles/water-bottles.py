class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """

            numBottles = 15 , numExch = 4        -> 3 -> 1 right 
            so 15 + 3 + 1 = 19
        
            print(15 // 4, 15 % 4, 6 // 4, 1 // 4)

        
        
        """

        drink = numBottles
        
        while numBottles // numExchange != 0 :
            drink += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange

            

        return drink