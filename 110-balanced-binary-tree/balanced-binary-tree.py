class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left is False: return False

            right = height(node.right)
            if right is False: return False

            if abs(left - right) > 1:
                return False

            return max(left, right) + 1

        return height(root) is not False
