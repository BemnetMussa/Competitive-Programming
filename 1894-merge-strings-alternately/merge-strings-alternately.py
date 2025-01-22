class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # abcd          docio
        # |                               1
        #               | 

        ptr = 0


        res = []
        while ( ptr < len(word1) and ptr < len(word2)):
            res.append(word1[ptr])
            res.append(word2[ptr])
            ptr += 1

        print(res)
        if (len(word1[ptr:]) > len(word2[ptr:])):
            res.append(word1[ptr:])

        elif ( len(word1[ptr:]) < len(word2[ptr:])):
            res.append(word2[ptr:])

        
        return ''.join(res)