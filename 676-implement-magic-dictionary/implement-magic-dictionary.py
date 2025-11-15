'''


functionalites it shoudl have
- MagicDictionary() intializing the object
- void buildDict(String[] dictionary) sets the diciotnary with distinct i array values
- bool search(String searchWord) return true if we can change one char in serachWord to match any stirng inside our datastrcutre reutrn true or false.

- bool search(String searchWord) 

iterating through collection then checking for each word the searchword characters if they equal there is one pass. 
'''

class MagicDictionary:

    def __init__(self):
        self.array = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.array = dictionary  # store the dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.array:
            if len(word) != len(searchWord):
                continue  # lengths must match
            mismatch = 0
            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    mismatch += 1
                    if mismatch > 1:
                        break
            if mismatch == 1:  # exactly one character differs
                return True
        return False # O(n * m)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)