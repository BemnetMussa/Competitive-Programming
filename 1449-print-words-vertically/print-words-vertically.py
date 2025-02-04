class Solution:
    def printVertically(self, s: str) -> List[str]:
        # [HOW, ARE, YOU]
        #  |    |     |         hay
        #   |    |    |         0ry
        #    |    |    |       weu

        # [To, be, or not to be]
        #  |   |   |  |   |  |     tbontb
        #                          Oerooe
        #                           


        ans = []

   

        i = 0
        s = s.split(" ")
        max_str = len(max(s, key=lambda x: len(x)))

     
        while i < max_str:
            store = ""
            for string in s:
           
                if i < len(string):
                    store += string[i]
                else:
                    store += ' '

            store = store.rstrip()
            ans.append(store)
            i += 1

        return ans