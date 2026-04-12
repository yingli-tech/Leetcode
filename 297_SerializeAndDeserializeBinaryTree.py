# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    # Sequence serialization: preorder traversal, mark null nodes as "null"
    def serialize(self, root):
        # This is a arrat of string
        res = []
        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Sequence deserialization: recursively build the tree, taking one value at a time
    def deserialize(self, data):
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()