# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy head to simplify edge cases
        v_head = ListNode(0)
        v_head.next = head
        # Traverse the linked list to obtain its length
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        num = 0
        temp = v_head    
        # Consider the required node is not in the linked list
        if length - n < 0: 
            return head

        # length - n
        while num < length - n:
            num += 1
            temp = temp.next
        # when the node to be deleted is the last one in the linked list    
        if temp.next is None or temp.next.next is None:
            temp.next = None
        else:
            temp.next = temp.next.next
        
        head = v_head.next
        return head