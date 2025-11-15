class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # requency of each numbers
        # and find the *frequency of the frequency of two numbers 
        # O(n), space of O(n)
        # contratins is 1000
        # arr = [1,2,2,1,1,3]
        # 1: 3, 2: 2, 3: 1
        # 3: 1, 2: 1, 1: 1

        freq = Counter(arr)
        freqOccurance = Counter(freq.values())

        for val in freqOccurance.values():
            if val > 1: # duplicate occurance
                return False

        return True