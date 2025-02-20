# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        

        dummy = ListNode(0, head)
        new = dummy
        curr = head

        # holding just the less ones in a new listnode
        while curr:
            if curr.val < x:
                new_node = ListNode(curr.val)
                new.next = new_node
                new = new.next
            curr = curr.next

            
        # then pointing the rest > x 
        curr = head
        while curr:
            if curr.val >= x:
                new_node = ListNode(curr.val)
                new.next = new_node
                new = new.next
            curr = curr.next
        
        return dummy.next
        

