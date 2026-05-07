# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        top = list1
        bottom = list2
        new_list = ListNode(0)
        current = new_list 

        while top is not None and bottom is not None:

            if top.val <= bottom.val:
                current.next= top
                top = top.next
            else:
                current.next= bottom
                bottom = bottom.next
            current = current.next
        if top is not None:
            current.next = top
        if bottom is not None:
            current.next = bottom

        return new_list.next

