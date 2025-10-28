class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        given word1 and word2 and merge the words into one single merge if there is a stirng is longer than the other. append the additonal eletters onto the end of the merged string. 
        return the merged string. 

        approch: - if the length of the other is greater just add it to the last of the concacted string

        "abc", "pqr"
         |     | 
         merge sort the mergeing part only()
        '''

        conc = ""

        ptr = ptr1 = 0
        alt = True
        while ptr < len(word1) and ptr1 < len(word2):
            if alt:
                conc += word1[ptr]
                ptr += 1

            else:
                conc += word2[ptr1]
                ptr1 += 1
            alt = not alt

        if ptr < len(word1):
            conc = conc + word1[ptr:]

        if ptr1 < len(word2):
            conc = conc + word2[ptr1:]

        return conc