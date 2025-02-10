class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:




        relativeSorted = []
        sortedd = []
        for i in arr2:
            for j in arr1:
                if (j == i):
                    relativeSorted.append(j)

        for i in arr1:
            if not(i in relativeSorted):
                sortedd.append(i)


        sortedd.sort()
            
        
        return relativeSorted + sortedd
