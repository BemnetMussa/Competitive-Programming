class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Let the recipes will be in order bread -> sandwich -> burger

        # we have supplies => yeast, flour, corn
        # req to make a bread = [yeast, flour] 
        # iterate on ingredients then if ingredients is fullfilled then add the bread in our supplies
        
        count = 0 # what can we make
        ans = []
        supplies = set(supplies) # for fast lookups O(1)

        while True:
            created_reci = False


            for i in range(len(recipes)):
                if recipes[i] in supplies:
                    continue
                for j in range(len(ingredients[i])):
                    if ingredients[i][j] not in supplies:
                        break
                else:
                    supplies.add(recipes[i])
                    ans.append(recipes[i])
                    created_reci = True

            # if we didn't create a recipe 
            if not created_reci:
                break



        return ans
            

            



