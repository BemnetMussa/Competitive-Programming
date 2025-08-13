class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:


        
        players.sort()
        trainers.sort()

        ptr = 0
        ptr2 = 0
        count = 0

        while (ptr < len(players) and ptr2 < len(trainers)):

            if players[ptr] <= trainers[ptr2]:
                count += 1
                ptr += 1
                ptr2 += 1

            elif players[ptr] > trainers[ptr2]:
                ptr2 += 1

        return count
        