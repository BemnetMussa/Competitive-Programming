class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        check the adjacent pixels if it is the same as source pixel then fill it by a color
        
        Approach:
        - start with the source pixel
        - check adjacent pixel (H and V)
        - fill it color if colors are the same
        
        doing one traversal -> efficient!
        '''

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        original = image[sr][sc]

        if original == color:  # if they are the same, no need to do anything
            return image

        def is_bound(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])

        def dfs(i, j):
            if not is_bound(i, j) or image[i][j] != original:
                return

            image[i][j] = color

            for ni, nj in directions:
                dfs(i + ni, j + nj)

        dfs(sr, sc)
        return image
