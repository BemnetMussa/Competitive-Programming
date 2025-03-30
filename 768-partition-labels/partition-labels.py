class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        


        s_counter = Counter(s)
        freq = 0
        curr = {}

        ans = []

        for char in s:

            if char not in curr:
                curr[char] = s_counter[char]
                freq += s_counter[char]

            freq -= 1

            if freq == 0:
                count = 0
                
                count += sum(s_counter[key] for key in curr)
                ans.append(count)
                curr.clear()
                freq = 0

        return ans