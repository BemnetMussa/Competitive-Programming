class Solution:
    def countVowels(self, word: str) -> int:
         # generating all the substrings will take -> n^2
         # by taking
            # in how many ways vowel will apear or be part of from the left and from the right

        count = 0
        for i, num in enumerate(word):
            if num in "aeiou":
                count += (i+1) * (len(word)-i)

        return count

           
