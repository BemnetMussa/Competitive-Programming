class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_counter = Counter(s)
        t_counter = Counter(t)

      

        count = 0

        if s_counter == t_counter:
            return 0

        for key in s_counter:
            while s_counter[key] != t_counter[key]:

                if s_counter[key] > t_counter[key]:
                    t_counter[key] += 1
                    count += 2
                    
                elif s_counter[key] < t_counter[key]:
                    t_counter[key] -= 1
                    count -= 1

        for ky in t_counter:
            if ky not in s_counter:
                count -= t_counter[ky]

        return count