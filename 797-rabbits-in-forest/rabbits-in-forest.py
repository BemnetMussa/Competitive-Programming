class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        

        rab = 0
        uniq = dict()



        for ans in answers:
            if ans == 0:
                rab += 1

            elif ans in uniq:
                uniq[ans] -= 1
                if uniq[ans] == 0:
                    del uniq[ans]
            else:
                rab += (ans + 1)
                uniq[ans] = ans


        
        return rab
                