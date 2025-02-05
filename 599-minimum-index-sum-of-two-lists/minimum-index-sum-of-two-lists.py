class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        

        least_index = float("inf")
        ans = []
        for i in range(len(list1)):

            for j in range(len(list2)):
                
                if list1[i] == list2[j]:
                    if least_index > (i + j):
                        ans.clear()
                        least_index = i + j
                        
                    elif least_index < (i + j):
                        continue

                    ans.append(list1[i])
                 
                

        return ans