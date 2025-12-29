class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        if N % 2 != 0:
            return -1

        # nive approch will take O(nlogn)
        # time taken --> 10^5
        # [3, 2, 5, 1, 3, 4] -> total = 18 // 3 = 6
        # hash = [ ]
        # 3 - 6 = abs(-3) = 3 x
        # 2- 6 = abs(-4]) = 4 X
        # 5 - 6 = abs(-1) = 1 X
        # 1 - 6 = abs(-5) = 5 corret -> 1
        # 3 - 6 = abs(-3) = 3 correct -> 2
        # 4 - 6 = abs(-2) = 2 correct -> 3
        # since -> 3 == len(skill) / 2 -> valid return true
        # Time -> O(n), space O(n/2) = O(n)

        total = sum(skill)
        target = total // (len(skill) // 2 )
        hashmap = Counter()
        teamUp = []

        for num in skill:
            difference = target - num
            if hashmap[difference] > 0:
                hashmap[difference] -= 1
                teamUp.append(difference * num)
            else:
                hashmap[num] += 1

        return sum(teamUp) if len(teamUp) == len(skill) // 2 else -1