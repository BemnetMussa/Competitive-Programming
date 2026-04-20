class Solution:
    def maxDistance(self, colors: List[int]) -> int:
       """
        Given: colors[i] list of houres with there repsective colors
        Requested: the deistance between two different colored houses
        Soltion: 
            Nive approch: Iterative through the colors for one color for each of the colors. keep track of the maximum
            Improved approch: 
                1 1 1 2 1 3 4 4 
                i         j                           1: (j - i)
                                                      2: (j - i) 
                                                      3: (j - i) ---> i should be dynamic also as a result value will not be enough it also the idx is important the earleist color 

            nive approch will pass since O(n^2) under 100 length only 
            best approch still O(n^2) so tha tis it i don't think there is more simpler one than this
       """ 

       max_length = 0
       for i in range(len(colors):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                      max_length = max(max_length, j-i)


# but clealry i don't need to calculate everything just checking the firs tand the last difference will be enough 
# worst case will be
                      11211
                      so on this case until it reaches the difference. so the middle and the last one or the middle the the first one it depends on the *odd factors also 

      for i in range(len(colors)):
        if colors[i] != colors[-1]:
            maxLength = max(max_length, len(colors) -  i)
        if colors[i] != colors[0]:
            maxLength = max(max_length, i+1)


        return max_length # this will run us O(n)
