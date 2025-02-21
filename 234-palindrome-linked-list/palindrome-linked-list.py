# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # using fast and slow approche
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # reverse the half of the linked list
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # comparing there values
        back = prev
        front = head

        while back:
            if back.val != front.val:
                return False
            front = front.next
            back = back.next

        return True


