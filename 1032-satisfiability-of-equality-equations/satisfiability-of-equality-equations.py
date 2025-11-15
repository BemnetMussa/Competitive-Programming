class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        def find(x):
            # with path compress
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
          
        parent = [i for i in range(26)]
        for e in equations:
            if e[1] == '=': # group them together 
               
                parent[find(ord(e[0]) - ord('a'))] = find(ord(e[3]) - ord('a'))

        # handle != case
        for e in equations:
            if e[1] == '!' and find(ord(e[0]) - ord('a')) == find(ord(e[3]) - ord('a')):
                return False
        return True