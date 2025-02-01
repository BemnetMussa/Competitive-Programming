class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        # [flower, flow, flight, f]
        #  |       |     |    
        #  flow
        # f   f ==> f
        # fl  fl ==> 

        # f f f == ignore
        # l l l == ignore flow
        # o o i == pop   flo
        # 


        if not strs:
            return ""
        prefix = strs[0]


        for s in strs[1:]:
            while not s.startswith(prefix) and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""

                
        return prefix