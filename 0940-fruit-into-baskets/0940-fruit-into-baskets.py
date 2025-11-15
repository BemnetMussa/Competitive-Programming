class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        

        window = Counter()

        left = 0
        length = float("-inf")

        for right in range(len(fruits)):
            window[fruits[right]] += 1

            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]

                left += 1

            length = max(length, right - left + 1)

        return length