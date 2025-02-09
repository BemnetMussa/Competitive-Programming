class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        

        rabbits = 0

        length = 0
        uniq = set()
        answers.sort()

        for ans in answers:
            if ans in uniq:
                if length == 0:
                    rabbits += (1 + ans)
                    length = ans
                else:
                    length -= 1

            else:
                rabbits += (1 + ans)
                length = ans
                uniq.add(ans)

        
        return rabbits
                