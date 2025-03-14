# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None  
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key) 
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) 
        else:

            if not root.left:
                return root.right
            if not root.right:
                return root.left 
            
            # Node has two children
            # Find the inorder successor (smallest in the right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val 
            root.right = self.deleteNode(root.right, successor.val)  
        
        return root  # Return the updated root
    
    def findMin(self, node):
        while node.left:
            node = node.left  # Go as far left as possible to find the minimum value
        return node
