# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder or not postorder:
            return None

        # Node1 is the inoder and node2 is the postorder
        def divide(node1, node2):
            if not node1 or not node2:
                return None
            # root
            # Every time you recurse, just do four things: 
            # 1. Create the root node for the current step, 
            # 2. Ensure there's a position for the left subtree node,
            # 3. Ensure there's a position for the right subtree node. 
            # 4. Return the root node.
            # Then, everything will fall into place.
            
            root_val = node2[-1] 
            root = TreeNode(root_val)

            # Location = list.index(value to be found in the list)
            # Index is internal function
            i = node1.index(root_val) 
       
            #last = len(node2) - 1
            #i = 0
            #while node1[i] != node2[last]:
            #    i += 1


            left_in = node1[:i]
            left_post = node2[:len(left_in)]
            
            right_in = node1[(i + 1) :]
            right_post = node2[len(left_in):-1]

            root.left = divide(left_in, left_post)
            root.right = divide(right_in, right_post)

            return root
        
        return divide(inorder, postorder)

        
