# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        # Getting the length of the linked list
        leng = 0
        while curr:
            leng += 1
            curr = curr.next

        # Number of full k-sized groups
        steps = leng // k

        # Swapping
        curr = head
        temp = None
        new_head = None  

        while curr and steps > 0:
            store = curr  
            before = self.reverse(curr, k) 

            if not new_head:
                new_head = before

            if temp:
                temp.next = before

            temp = store 
            curr = store.next  

            steps -= 1

        return new_head if new_head else head  

    def reverse(self, head, k):
        before = None
        curr = head
        temp = head
        index = 0

        while index < k and curr:
            curr = curr.next
            temp.next = before
            before = temp
            temp = curr
            index += 1

        head.next = curr
        return before
