class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed_size = len(flowerbed)
        for i in range(flowerbed_size):
            if n <= 0:
                break
            prev = i == 0 or flowerbed[i - 1] == 0
            fut = i == flowerbed_size - 1 or flowerbed[i + 1] == 0
            if prev and fut and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0