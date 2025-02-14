class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        minimum_sub = s*10
   
        dict_t = Counter(t)

        dict_valid = {}
        

        left = 0
        for right in range(len(s)):

            if s[right] in dict_t:
                dict_valid[s[right]] = 1 + dict_valid.get(s[right], 0)

            while dict_valid.keys() == dict_t.keys():
               
                for key in dict_t.keys():
                 
                    if dict_valid[key] < dict_t[key]:
                        break
                
                else:
                    if right-left + 1 < len(minimum_sub):
                        minimum_sub = s[left:right + 1]

                    if s[left] in dict_valid.keys():
                        dict_valid[s[left]] -= 1
                        if dict_valid[s[left]] == 0:
                            del dict_valid[s[left]]

                    left += 1

                    continue
                break
            

        return minimum_sub if len(minimum_sub) != len(s*10) else ""

    



