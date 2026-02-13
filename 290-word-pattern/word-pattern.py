class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       
       # "abba"   "dog dog dog dog"
       # a --> dog
       # b ==> dog
       # it should be one char to one word 

        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        map_char_word = {}
        map_word_char = {}

        for char, word in zip(pattern, words):
            if char in map_char_word and map_char_word[char] != word: # freq not the same
                return False
            if word in map_word_char and map_word_char[word] != char:
                return False

            map_char_word[char] = word
            map_word_char[word] = char

        return True