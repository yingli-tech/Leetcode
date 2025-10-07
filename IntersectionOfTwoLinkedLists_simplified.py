# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        while pA != pB:
            # 如果走到头，就切换到另一个链表
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA  # 相遇点就是交点，或者都是None

