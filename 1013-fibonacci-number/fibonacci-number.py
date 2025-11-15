class Solution:

    def __init__(self):
        self.hashmap = defaultdict(int)

    def fib(self, n: int) -> int:
       
        if n == 0:
            return 0
        if n == 1:
            return 1

        if self.hashmap[n]:
            return self.hashmap[n]

        # tracking already build one
        self.hashmap[n] = self.fib(n-1) + self.fib(n-2)

        return self.hashmap[n]

        # 3 , 4, 
        # 0, 1, 1, 2
    