'''
Given: word: string, 

Requested: to remove one letter from the word by intenstion of making frequency of each char in the word equal.
 - **Must remove a char

Constratins: 
2 <= word.length <= 100
word only lower case english letters. 

Approch: 
    word = "abccde"
        ['a': 1, 'b': 1, 'd': 1, 'e': 1, 'c': 2, 'z': 2]
        [1: 4, 2: 2,] -> *frequency of the frequency_char, 
            --> 4 char that are appers 1, and there is 1 char that have frequency of 2
        remove c will give as [1: 5]
    "abcccde"
        ['a': 1, 'b': 1, 'd': 1, 'e': 1, 'c': 3]
        [1: 4, 3: 1] -> *frequency of the frequency_char, 
        remove *one c will not gurante equals since 2: 1. so --> difference abs(1, 3) > 1 so wrong
    "abcde"
        ['a': 1, 'b': 1, 'd': 1, 'e': 1, 'c': 1]
        [1: 5] -> *frequency of the frequency_char, 
        remove just one and still the same so good  **

    
word = "aazz"
        ['a': 2, 'z': 2]
        [2: 2],
        remove one  since equal 2 == 2 return false

# alot of test cases that we need to consider. 
what if i iterate through the word chars then remove one char then check if they are equal 
or not , then restore it then try again


'''

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)

        for char in word:
            freq[char] -= 1
            if freq[char] == 0: # remove char
                del freq[char] 

            values = set(freq.values())
            if len(values) == 1:
                return True # by removing one char it satisfied

            # if not, restore
            freq[char] = freq.get(char, 0) + 1

        return False

            