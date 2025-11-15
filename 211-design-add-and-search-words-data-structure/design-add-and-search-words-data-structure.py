'''
string on a set and iterating and for each . reovme it and add it 

"abc" add
".bc", "a.c", "..c"
using trie nodee bbyyyy
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            if word[i] == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False
        
        return dfs(self.root, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)