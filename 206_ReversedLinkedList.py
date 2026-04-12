# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return None
        previous = head
        current = head.next
        head.next = None
        while current:
            latter = current.next
            current.next = previous
            head = current
            previous = current
            current = latter
        
        return head