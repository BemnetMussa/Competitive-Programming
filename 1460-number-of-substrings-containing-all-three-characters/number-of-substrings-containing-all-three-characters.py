class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        left = 0
        window_dict = defaultdict(int)

        subString_count = 0

        for right in range(len(s)):
            window_dict[s[right]] += 1

            while len(window_dict) == 3:
                subString_count += len(s) - right

            
                window_dict[s[left]] -= 1
                if window_dict[s[left]] == 0:
                    del window_dict[s[left]]

                left += 1

        return subString_count
