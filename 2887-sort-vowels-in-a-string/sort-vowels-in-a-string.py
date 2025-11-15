class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u']

        res = []
        temp = []
        for char in s:
            if char.lower() in vowels:
                res.append(-1)
                temp.append(char)
            else:
                res.append(char)
        
        temp.sort()
        x = 0
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = temp[x]
                x += 1
        
        return "".join(res)
