# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        tail = None
        carry = 0

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            sum = val_1+val_2+carry
            val= sum%10
            carry = sum//10
            node = ListNode(val)
            if not dummy:
                dummy=node
                tail = node
            else:
                tail.next = node
                tail = node

            if  l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        
        return dummy
        

