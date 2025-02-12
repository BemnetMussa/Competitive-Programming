class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        left = 1
        right = len(skill)-2

        chem = skill[0] + skill[-1]


        prod = skill[0] * skill[-1]
        while left < right:

            if skill[left] + skill[right] == chem:
                prod += (skill[left] * skill[right])
            else:
                return -1
            left += 1
            right -= 1


        return prod


            
