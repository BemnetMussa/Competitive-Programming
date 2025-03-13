class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        res = [1]

        for i in range(rowIndex):
            arr = [0] * (len(res) + 1)
            for j in range(len(res)):
                arr[j] += res[j]
                arr[j+1] += res[j]

            res = arr



        return res