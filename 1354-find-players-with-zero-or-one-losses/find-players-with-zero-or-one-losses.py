class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
        #   | |   

        winner = dict()
        loser = dict()




        for match in matches:
            winner[match[0]] = winner.get(match[0], 0) + 1
            loser[match[1]] = loser.get(match[1], 0) + 1


        w = set(winner) - set(loser)
        l = [i for i in loser.keys() if loser[i] == 1]
        
        
        l.sort()
        
        w = list(w)

        w.sort()


        return [w, l]
       


        
