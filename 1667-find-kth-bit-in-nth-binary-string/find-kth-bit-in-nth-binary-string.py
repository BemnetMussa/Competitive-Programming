class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        # recursive nature
        def reco(binaryString, n):
            if n == 1:
                return binaryString

            # operation
            invertedString = ["1" if char == "0" else "0" for char in binaryString ]
            newString = binaryString + "1" + "".join(invertedString[::-1])
        
            return reco(newString, n-1)

   
        return reco("0", n)[k-1]

            