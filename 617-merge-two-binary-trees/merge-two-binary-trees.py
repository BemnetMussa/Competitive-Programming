# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1

        def bfs(node1, node2):
            if not node2 and not node1:
                return 
            elif not node1:
                return node2
            elif not node2:
                return node1
            
            node2.val = node2.val + node1.val  
            node2.left = bfs(node1.left, node2.left)
            node2.right = bfs(node1.right, node2.right)

            return node2
        
        return bfs(root1, root2)