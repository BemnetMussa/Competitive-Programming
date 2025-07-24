# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                self.balanced = False

            return max(left, right) + 1

        height(root)
        return self.balanced
