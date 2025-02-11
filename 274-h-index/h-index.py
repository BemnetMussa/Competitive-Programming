class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()

        freq = [0] * (len(citations)+1)

        citation = 0
     
        for i in range(len(citations)):

            if citations[i] >= len(freq):
                freq[-1] += 1
            else:
                freq[citations[i]] += 1
        print(freq)
        for i in range(len(freq)-2, -1, -1):
            freq[i] += freq[i+1]
        print(freq)

        for i in range(len(freq)-1, -1, -1):
            if i <= freq[i]:
                return i

        # left = 0
        # right = len(citations) -1

        # while (left <= right):
        #     mid = (left + right) // 2

        #     if citations[mid] >= len(citations) - mid:
        #         right = mid - 1

        #     else:
        #         left = mid + 1

        # return  len(citations) - left