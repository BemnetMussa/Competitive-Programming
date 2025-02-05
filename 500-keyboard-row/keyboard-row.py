class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        

        firstRow_set = set("qwertyuiop")
        secondRow_set = set("asdfghjkl")
        thridRow_set = set("zxcvbnm")


        a_key = [firstRow_set, secondRow_set, thridRow_set]


        res = []
        for word in words:
            word_counter = set(word.lower())

            for key in a_key:
                
                # if subset of key
                if  word_counter <= key:
                    res.append(word)

        return res


        