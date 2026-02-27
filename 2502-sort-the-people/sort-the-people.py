class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        merge_names_heights = list(zip(names, heights))
        merge_names_heights.sort(key=lambda x: x[1], reverse=True)
        return [names for names, _ in merge_names_heights]