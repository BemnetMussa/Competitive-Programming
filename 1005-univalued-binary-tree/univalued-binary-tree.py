# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])  

        while queue:
            node = queue.pop()
            
            if node.left:
                if node.left.val != node.val:
                    return False
                queue.append(node.left)
            if node.right:
                if node.right.val != node.val:
                    return False
                queue.append(node.right)
            
        return True
            