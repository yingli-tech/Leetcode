class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        # 创建中序遍历值的索引映射，提高查找效率
        inorder_index_map = {}
        for idx, val in enumerate(inorder):
            inorder_index_map[val] = idx
        
        def build(pre_start, pre_end, in_start, in_end):
            """使用索引范围而不是切片来构建树"""
            # 基准情况
            if pre_start > pre_end or in_start > in_end:
                return None
                
            # 根节点是前序遍历的第一个元素
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            idx = inorder_index_map[root_val]
            
            # 计算左子树的大小
            left_size = idx - in_start
            
            # 递归构建左右子树
            root.left = build(
                pre_start + 1,              # 左子树在前序遍历中的开始
                pre_start + left_size,      # 左子树在前序遍历中的结束
                in_start,                   # 左子树在中序遍历中的开始  
                idx - 1                     # 左子树在中序遍历中的结束
            )
            
            root.right = build(
                pre_start + left_size + 1,  # 右子树在前序遍历中的开始
                pre_end,                    # 右子树在前序遍历中的结束
                idx + 1,                    # 右子树在中序遍历中的开始
                in_end                      # 右子树在中序遍历中的结束
            )
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)