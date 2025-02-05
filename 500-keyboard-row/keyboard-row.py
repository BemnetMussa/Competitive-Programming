class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        

        firstRow_set = set("qwertyuiop")
        secondRow_set = set("asdfghjkl")
        thridRow_set = set("zxcvbnm")


        a_key = [firstRow_set, secondRow_set, thridRow_set]


        res = []
        for word in words:
            word_counter = set(word.lower())

            # if subset of row keys
            if  word_counter <= firstRow_set or word_counter <= secondRow_set or word_counter <= thridRow_set:

                res.append(word)

        return res


        