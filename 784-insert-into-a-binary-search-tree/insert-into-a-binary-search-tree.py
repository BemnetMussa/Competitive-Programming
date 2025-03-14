# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(node, val):
            
    

            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
        if not root:
            return TreeNode(val)
            
        insert (root, val)
        return root



        