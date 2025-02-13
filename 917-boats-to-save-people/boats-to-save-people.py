class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        boat = 0
        people.sort()
        ptr = 0
        ptr1 = len(people) - 1

        while ptr <= ptr1:
            if people[ptr] + people[ptr1] <= limit:
                ptr += 1
            ptr1 -= 1
            boat += 1

        return boat
