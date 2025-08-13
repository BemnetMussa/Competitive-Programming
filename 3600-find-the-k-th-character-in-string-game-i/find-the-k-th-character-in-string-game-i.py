class Solution:
    def kthCharacter(self, k: int) -> str:
        '''
            given: word ( string )

            req: the Kth character

            operation: convert the word to the next words of each character and append it then after that append it to the word each time at least to get kth charcter

            constraing: 500

            approach: it will be straight forward. nothing. 
                everything it doubles right the num of character so 
                    for example: "b" with k = 5 it will double how many times 3 times then it reaches 8 length that is why
                    1 -> 2 -> 4 -> 8 ok we know find it easy knwow what how t oknow that charcter
        '''
        word = ['a']
        print(ord('a'))
        def convert(s):
            new = []
            for char in word:
                order = ord(char) - 97 + 1
                next_char =  order + 1 if order != 26 else 1
           
                new_char  = chr(next_char + 97 - 1)
                new.append(new_char)

            word.extend(new)
        while len(word) <= k:
            convert(word)


        return word[k-1]

