# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        dummy=None
        tail=None
        
        while list1 and list2:
            if list1.val>=list2.val:
                chosen=list2
                list2=list2.next
            else:
                chosen=list1
                list1=list1.next
            
            if dummy is None:
                dummy=chosen
                tail=chosen
            else:
                tail.next=chosen
                tail=chosen
        
        if list1:
            tail.next=list1
        else:
            tail.next=list2
        
        return dummy
        