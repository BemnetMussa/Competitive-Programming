# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        # using que to track the elvelllll

        que = deque([root])
        res = []

        while que:
            level_max = float('-inf')
            for _ in range(len(que)):
                node = que.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.append(level_max)

        return res
