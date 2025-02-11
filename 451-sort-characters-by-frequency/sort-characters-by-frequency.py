class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)

        sorted_chars = sorted(freq , key=lambda x: freq[x], reverse=True)

        return "".join(char * freq[char] for char in sorted_chars)