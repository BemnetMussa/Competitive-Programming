class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        


        ans = [name for name , _ in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]

        return ans