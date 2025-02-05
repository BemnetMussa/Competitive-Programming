class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        

        least_index = float("inf")
        ans = []

        list1_dict = {}

        for index, val in enumerate(list1):
            list1_dict[val] = index


        for index, val in enumerate(list2):
            
            if val in list1:
                sum_index = index + list1_dict[val]
                if val == list1[list1_dict[val]]:
                    if sum_index < least_index:
                        ans.clear()
                        least_index = sum_index
                        ans.append(val)
                    
                    elif sum_index == least_index:
                        ans.append(val)



        return ans