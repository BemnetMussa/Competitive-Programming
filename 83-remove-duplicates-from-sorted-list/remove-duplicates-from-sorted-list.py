class Solution:
    def deleteDuplicates(self, head):
        new = ListNode(0) 
        dummy = new  

        unique = []  # List to keep track of unique values

     
        while (head != None):
            if not(head.val in unique):  
                unique.append(head.val)  # 
            head = head.next 

        for i in unique:
            dummy.next = ListNode(i)  
            dummy = dummy.next  

        dummy = None  

        return new.next 
