class ListNode: 
    def __init__(self, val: int, next = None): 
        self.val = val 
        self.next = next 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = ListNode(1) 
        tmp = head 

        # setting up the linked list 
        for i in range(2, n + 1): 
            tmp.next = ListNode(i)
            tmp = tmp.next 

        # edge case: temp = head 
        if tmp.val == head.val: 
            return 1
        
        tmp.next = head # cycle linked list 
        prev = tmp 
        curr = tmp.next 

        for _ in range(n - 1): 
            for _ in range(k - 1): 
                # traversing (k - 1) nodes
                prev = prev.next 
                curr = curr.next 
            # deleting loser 
            prev.next = curr.next 
            curr = curr.next 
        
        return curr.val 
