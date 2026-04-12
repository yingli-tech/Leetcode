# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # set up a virtual head 
        # to ensure processing the head is the same as the other nodes 
        ying = ListNode(1)
        ying.next = head
        present = ying

        while present.next is not None:
            current = present.next
            if current.val == val:
                present.next = current.next
            # remember to update the pointer
            else:
                present = present.next
         
        return ying.next

            
