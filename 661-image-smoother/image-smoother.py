
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        new_img = deepcopy(img)


        for i in range(len(img)):
            for j in range(len(img[i])):
    
                avg_value = self.imageScanner(img, i, j)
                # Update the pixel in the new image
                new_img[i][j] = avg_value

        return new_img


    def imageScanner(self, img, r, c):
        # List to store the values of neighbor cells
        neighbors = []

   
        for i in range(r - 1, r + 2): 
            for j in range(c - 1, c + 2): 
    
                if 0 <= i < len(img) and 0 <= j < len(img[0]):
                    neighbors.append(img[i][j])


        return sum(neighbors) // len(neighbors)
