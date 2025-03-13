# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, arr):
        if not node:
            return []

        self.dfs(node.left, arr)
        self.dfs(node.right, arr)
        arr.append(node.val)
        return arr

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root, [])
      