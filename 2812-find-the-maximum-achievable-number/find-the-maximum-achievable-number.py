class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # x is achivable if x == num and only if operations at most t times
        
        """
            operations of x
                ++ or -- > x and ++ or -- > num  (which is t times)

            at last return the max value of x


            soln

                num = 4  , t = 1

                num += 1  and x -= 1


                num = 3 and t = 2

                num += 1 and x 

                

        """

        return num + (t + t)

