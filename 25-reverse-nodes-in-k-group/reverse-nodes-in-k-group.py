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
        prev, curr = None, head
        while k > 0:
            curr.next, prev, curr = prev, curr, curr.next
            k -= 1
        head.next = curr
        return prev