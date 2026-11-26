# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count_nodes(self, root: TreeNode, max_val: int) -> int:
        if not root:
            return 0
        cur_node_count = 0
        if root.val >= max_val:
            max_val = root.val
            cur_node_count += 1
        left = self.count_nodes(root.left, max_val)
        right = self.count_nodes(root.right, max_val)
        return left + right + cur_node_count

    def goodNodes(self, root: TreeNode) -> int:
        result = self.count_nodes(root, root.val)
        # if result > 1:
        #     result += 1
        
        return result