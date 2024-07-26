# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = head, head 

        while j and j.next: 
            i = i.next 
            j = j.next.next 
            if i == j: 
                # reset pointer and follow hare-tortoise algo
                i = head 
                while i != j: 
                    i = i.next 
                    j = j.next
                return i
        return None 
