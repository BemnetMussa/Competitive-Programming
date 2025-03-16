# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, left, right, level):
        if not left:
            return 

        if level % 2 == 0:
            left.val, right.val = right.val, left.val

        level += 1
        self.bfs(left.left, right.right, level )
        self.bfs(left.right, right.left, level )


    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root or not root.left:
            return root

        # call the bfs
        self.bfs(root.left, root.right, 2)

        return root
        