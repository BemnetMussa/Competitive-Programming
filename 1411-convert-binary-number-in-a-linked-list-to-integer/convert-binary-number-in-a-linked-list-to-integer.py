# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        number = []

        curr = head
        while curr:
            number.append(str(curr.val))
            curr = curr.next

        integer = int(''.join(number), 2)

        return integer