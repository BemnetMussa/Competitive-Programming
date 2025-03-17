# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root:
            return 0

        return self.dfs(root, root.val, root.val, 0)

    def dfs(self, node, curr_max, curr_min, zmax):
        if not node:
            return curr_max - curr_min

        curr_max = max(node.val, curr_max)
        curr_min = min(node.val, curr_min)
        print(node.val, curr_max, curr_min)

        left_max = self.dfs(node.left, curr_max, curr_min, zmax)
        right_max = self.dfs(node.right, curr_max, curr_min, zmax)
        
        return max(left_max, right_max)
