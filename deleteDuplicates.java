class Solution 
{
    public ListNode deleteDuplicates(ListNode head) 
    {
        ListNode pointer = head; 
        while (pointer != null && pointer.next != null) {
            int currVal = pointer.val;
            int nextVal = pointer.next.val;
            if (currVal == nextVal) {
                pointer.next = pointer.next.next;
            }
            else {
                pointer = pointer.next; 
            }
        }
        return head; 
    }
}
