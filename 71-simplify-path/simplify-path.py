class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        A single period '.' represents the current directory.
        A double period '..' represents the previous/parent directory.
        Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
'''

        paths = path.split('/')
        stack = []
        print(paths)

        for char in paths:
            if char == "/" or char == "." or char == "":
                pass
            
            elif char == "..":
                if stack:
                    stack.pop()
                
            else:
                stack.append(char)

       
        return "/" + "/".join(stack)

