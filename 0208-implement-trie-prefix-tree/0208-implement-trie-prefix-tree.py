# define the TrieNode()
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False # word not found
            node = node.children[char]

        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True

    
    def delete(self, word: str) -> True:
        def _delete(node, word, depth):
            # if the depth is reached
            if depth == len(word):
                if not node.is_end:
                    return False

                node.is_end = False
                return len(node.children) == 0 # pop it
            
         
            char = word[depth]

            if char not in node.children:
                return False

            should_be_deleted = _delete(node.children[char], word, dpeth + 1)

            if should_be_deleted:
                del node.children[char]
                return not node.is_end and len(node.children) == 0

            return False

        _delete(self.root, word, 0)
            


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)