class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        

        ans = []

        for word in words:
            for i in word:
                if chars.count(i) < word.count(i):
                    break
            else:
                ans.append(len(word))


        return sum(ans)






