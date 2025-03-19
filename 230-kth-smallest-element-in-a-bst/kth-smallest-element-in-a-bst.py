class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k  
        self.result = None 
        
        def dfs(node):
            if not node or self.result is not None:
                return  

            dfs(node.left)  

            self.count -= 1
            if self.count == 0:
                self.result = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return self.result
