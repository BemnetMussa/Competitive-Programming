# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        Approach: sum values on even levels vs odd levels.
        - Even levels: 0, 2, 4 ...
        - Odd levels: 1, 3, 5 ...
        Return max of the two sums.
        """
        def dp(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dp(node.left)
            right = dp(node.right)

            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dp(root))
