class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        stack = []
        t = 0

        s1_counter = Counter(s1)
        k = len(s1)
        s2_counter = Counter(s2[:k])

        if s2_counter == s1_counter:
            return True

        for i in range(k, len(s2)):

            
            s2_counter[s2[i]] += 1
           

            s2_counter[s2[i-k]] -= 1
            if s2_counter[s2[i-k]] == 0:
                del s2_counter[s2[i-k]]

            if s2_counter == s1_counter:
                return True


        return False