# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       # using Breadth first serach (BFS)
        result = []
        queue = deque([root] if root else [])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                # at most 2 childs
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        
        # reverse the odd levels
        for i in range(len(result)):
            if i % 2:
                result[i] = list(reversed(result[i]))

        return result