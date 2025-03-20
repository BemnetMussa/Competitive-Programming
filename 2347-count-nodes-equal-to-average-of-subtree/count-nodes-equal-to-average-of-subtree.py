class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0  # Count node.val == average

        def dfs(node):
            nonlocal count  
            if not node:
                return (0, 0)  # Return (sum, number of nodes)

            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_nodes = left_nodes + right_nodes + 1

            if node.val == total_sum // total_nodes:
                count += 1

            return (total_sum, total_nodes)

        dfs(root)
        return count
