class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        


        s_counter = Counter(s)
        freq = 0
        curr = []

        ans = []

        for char in s:
            if char in curr:
                curr.append(char)
                freq -= 1

            else:
                curr.append(char)
                freq += s_counter[char]
                freq -= 1

            if freq == 0:
                ans.append(len(curr))
                curr.clear()
                

        
        return ans