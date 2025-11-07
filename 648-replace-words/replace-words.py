class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        fast_lookup = set(dictionary)

        res = []
        sentence = list(sentence.split(" "))
        for word in sentence:
            prefix = ""
            replaced = False
            for char in word:
                prefix += char
                if prefix in fast_lookup:
                    replaced = True
                    break

            if replaced:
                res.append(prefix)
            else:
                res.append(word)
        
        return " ".join(res)



