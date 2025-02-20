from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0, head)
        left = dummy
        right = head
    
        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        # Move both left and right pointers together until right reaches the end
        while right:
            left = left.next
            right = right.next
        
        # Remove the nth node from the end
        left.next = left.next.next
        
        return dummy.next
