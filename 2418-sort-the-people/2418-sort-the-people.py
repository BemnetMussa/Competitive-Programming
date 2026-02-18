class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # merge_names_heights = list(zip(names, heights))
        # merge_names_heights.sort(key=lambda x: x[1], reverse=True)
        # return [names for names, _ in merge_names_heights] # time compelxity: O(nlogn), space complexity: O(n)

        unsorted_last_index = len(names) - 1
        for i in range(unsorted_last_index, -1, -1):
            for j in range(i-1, -1, -1):
                if heights[i] > heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]

        return names # time compelxity: O(n^2) , space xomplcity: O(1)