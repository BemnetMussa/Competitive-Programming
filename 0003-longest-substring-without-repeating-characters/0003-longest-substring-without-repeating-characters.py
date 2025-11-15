class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0 # keep track of the max length

        frequency = defaultdict(int) # frequency of char

        left = 0
        for right in range(len(s)):
            char = s[right]
            frequency[char] += 1

            while frequency[char] > 1: # shrink the window
                char_left = s[left]

                frequency[char_left] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length # time_complexity 