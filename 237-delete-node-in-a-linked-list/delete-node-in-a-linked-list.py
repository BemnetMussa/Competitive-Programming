class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Swap the current node's value with the next node's value
        while node and node.next:
            preVal = node.val
            node.val = node.next.val
            node.next.val = preVal
            

            if not node.next.next: 
                node.next = None
                break
            else:
                node = node.next
