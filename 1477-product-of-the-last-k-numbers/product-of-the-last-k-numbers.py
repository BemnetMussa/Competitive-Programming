class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prefix_total = 1
        self.zero = "$"
        self.length = 0
        

    def add(self, num: int) -> None:

        if num != 0:
            self.prefix_total *= num
            self.arr.append(num/self.prefix_total)

        else:
            self.prefix_total = 1
            self.arr.append(0)
            self.zero = self.length - 1

  
        self.length += 1

            

    def getProduct(self, k: int) -> int:
        index = self.length - k
        ans = self.arr[index] * self.prefix_total
     
        if self.zero == "$":
            return math.ceil(ans)
        else:
            if self.zero < index:
                return math.ceil(ans)
            else:
                return 0



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)