# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def trav(node, val):

            if node:
                if node.val == val:
                    return node

                elif node.val > val:
                    return trav(node.left, val)
                else:
                    return trav(node.right, val)

            return None

        
        return trav(root, val)




