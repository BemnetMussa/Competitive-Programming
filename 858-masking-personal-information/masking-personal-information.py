import re

class Solution:
    def maskPII(self, s: str) -> str:
        # handling the email part
        if "@" in s:
            li = s.split("@")
            print(li)
            li[0] = li[0][0].lower() + "*" * (5) + li[0][-1].lower()
            return "".join([li[0], "@", li[1].lower()])  


        # handling phonenumber part
        digits = re.sub(r'\D', '', s)  
        country_code = len(digits) - 10  
        ans = ""


        if country_code > 0:
            ans += "+" + "*" * country_code + "-"

      
        ans += "***-***-" + digits[-4:]  
        return ans
