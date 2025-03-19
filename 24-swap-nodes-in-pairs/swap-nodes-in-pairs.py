# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = head

        curr = dummy

        while curr and curr.next:

            temp = curr.next.val
            curr.next.val = curr.val
            curr.val = temp

            curr = curr.next.next


        return dummy
