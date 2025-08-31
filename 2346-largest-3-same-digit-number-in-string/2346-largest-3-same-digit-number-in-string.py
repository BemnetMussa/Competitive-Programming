class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        hash = defaultdict(int)

        zmax = -1
      
        for right in range(len(num)):
            number = num[right]

            if number in hash:
                hash[number] += 1
                if hash[number] == 3:
                    zmax = max(zmax, int(number))
            else:
                hash.clear()
                hash[number] = 1

        print(zmax)
        return str(zmax) * 3 if zmax != -1 else ""