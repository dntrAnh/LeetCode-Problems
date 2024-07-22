# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        
        new_list = ListNode(0)
        current = new_list
        curr_sum = 0
        
        while head:
            if head.val == 0:
                current.next = ListNode(curr_sum)
                current = current.next
                curr_sum = 0
            else:
                curr_sum += head.val
            
            head = head.next
        
        return new_list.next
