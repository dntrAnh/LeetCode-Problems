# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        result = [-1, -1]
        min_dist = float("inf") 

        prev_node = head
        curr_node = head.next
        next_node = curr_node.next
        curr_idx = 1
        prev_critical_idx = -1
        first_critical_idx = -1

        while next_node:
            if (curr_node.val < prev_node.val and curr_node.val < next_node.val) or \
               (curr_node.val > prev_node.val and curr_node.val > next_node.val):
                if prev_critical_idx == -1:
                    prev_critical_idx = curr_idx
                    first_critical_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_critical_idx)
                    prev_critical_idx = curr_idx

            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next
            curr_idx += 1

        if prev_critical_idx != first_critical_idx:
            max_dist = prev_critical_idx - first_critical_idx
            result = [min_dist, max_dist]

        return result
