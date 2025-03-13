# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, ans):
        if not node:
            return []
        self.dfs(node.left, ans)
        ans.append(node.val)
        self.dfs(node.right, ans)
        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        return self.dfs(root, [])
        