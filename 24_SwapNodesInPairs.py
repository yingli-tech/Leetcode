# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        v_head = ListNode(0)
        v_head.next = head
        pre_pre = v_head
        pre = head
        current = head.next
	#this condition is very direct
        while current and pre:
	#swap nodes and notice the adjoint location
            latter = current.next
            pre.next = latter
            pre_pre.next = current    
            current.next = pre
            #update the pointers, the increasement is 2 
            pre_pre = pre
            pre = latter 
            current = latter.next if latter else None
        head = v_head.next
        return head