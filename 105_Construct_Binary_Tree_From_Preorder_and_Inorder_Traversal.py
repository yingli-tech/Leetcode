# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # Node1 is the preorder and node2 is the inorder
        def divide(node1, node2):
            if not node1 or not node2:
                return
            # Create a root each time
            root_val = node1[0]
            root = TreeNode(root_val)

            idx = node2.index(root_val)
            # Divide the list to have left subtree and right subtree
            left_in = node2[:idx]
            right_in = node2[idx + 1:]

            left_pre = node1[1:len(left_in) + 1]
            right_pre = node1[len(left_in) + 1:]

            root.left = divide(left_pre, left_in)
            root.right = divide(right_pre, right_in)

            return root

        return divide(preorder, inorder)