class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        #  bank = ["011001","000000","010100","001000"]
        #            ||  |                              -> 3
        #                              | |              _. 3 * 2 = 6
        #                              | |        |     -> 2 * 1 += 8

        # store the prvious count of ones and add it into res

        res = 0
        stack = [] # store the preivous counts

        ROWS, COLS = len(bank), len(bank[0])

        for i in range(ROWS):
      
            count = bank[i].count("1")
            print(count)
            if stack and count > 0:
                res += stack[-1] * count

            if count > 0:
                stack.append(count)
                
        return res