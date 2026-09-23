# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node is None:
                return -1
            left = height(node.left)
            right = height(node.right)
            if left == -2 or right == -2:
                return -2

            if abs(left - right) > 1:
                return -2

            return max(left, right) + 1
        
        return height(root) != -2