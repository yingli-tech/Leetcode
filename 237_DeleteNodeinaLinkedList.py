# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        latter = node.next
        node.val = latter.val
        node.next = latter.next
        del latter