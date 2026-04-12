# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        v_head = ListNode(0)
        v_head.next = head
        current = v_head
        num = 0
        while current and num < left:
            num += 1
            # record the position of left - 1
            record_previous = current
            current = current.next
        # Store the tail node of the split segment
        record_list = current
        
        if left == right:
            return v_head.next

        pre = current
        temp_current = current.next
        num += 1   
        while pre and temp_current and num <= right:
            latter = temp_current.next
            temp_current.next = pre
            pre = temp_current
            temp_current = latter
            num += 1
        
        record_previous.next = pre
        record_list.next = temp_current
        
        return v_head.next