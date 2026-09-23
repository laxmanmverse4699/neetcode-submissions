# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # check at each node, is it the max length between two sides of the nodes.
        self.diameter = 0

        def height(node):
            if node is None:
                return -1
            left = height(node.left)
            right = height(node.right)

            self.diameter = max(self.diameter, left + right + 2)
            # written the longest side to the parent.
            return max(left, right) + 1
        height(root)
        return self.diameter