class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        ans = {}


        for domains in cpdomains:
            cp_domain = domains.split(" ")
            # [9001, dicuss.leetcode.com]

            domain = cp_domain[1].split(".")
            # [discuss, leetcode, com]

            for d in range(len(domain)-1, -1, -1):
           
                store = ".".join(domain[d:])

                ans[store] = ans.get(store, 0) + int(cp_domain[0])
              
        res = []

        for de in ans:
            val = str(ans[de]) + " " + de
            res.append(val)

        return res