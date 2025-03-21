# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # inorder traversal
        arr = []

        def inorder(node):
            if node:
                inorder(node.left)          
                arr.append(node.val)
                inorder(node.right)

        
        # to get the inorder traversal of BST
        inorder(root)
    
        # constracting a new tree
        def bfs(node, inorder):
            if not inorder:
                return None

            mid = len(inorder) // 2
            node = TreeNode(inorder[mid]) 
            node.left = bfs(node.left, inorder[:mid])  
            node.right = bfs(node.right, inorder[mid+1:]) 

            return node  

        return bfs(None, arr)
