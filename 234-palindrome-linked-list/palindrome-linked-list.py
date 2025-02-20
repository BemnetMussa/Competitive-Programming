# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        
        first = head
        li = []
        i = -1
        while(head != None):
            li.append(head.val)
  
            head = head.next


        
        while(first != None):
            if first.val != li[i]:
                return False
            first = first.next
            i -= 1
        return True
            
