# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        curA, curB = headA, headB
        
        # let the pointer of longer linked-list take the steps of the length difference
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        else:
            for _ in range(lenB - lenA):
                curB = curB.next
        
        # move forward simultaneously, and look for the intersection node
        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA  
        # If there is an intersetion node, return the node. If not, return None.    

