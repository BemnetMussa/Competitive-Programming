class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        

        firstRow_counter = Counter("qwertyuiop")
        secondRow_counter = Counter("asdfghjkl")
        thridRow_counter = Counter("zxcvbnm")


        a_key = [firstRow_counter, secondRow_counter, thridRow_counter]


        res = []
        for word in words:
            word_counter = Counter(word.lower())
            
            for key in a_key:
                if  word_counter.keys() <= key.keys():
                    res.append(word)

        return res


        