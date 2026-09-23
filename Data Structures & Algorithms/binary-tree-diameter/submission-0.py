# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple
class Solution:
    def helper(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root is None:
            return -1, 0

        left_height, left_dia = self.helper(root.left)
        right_height, right_dia = self.helper(root.right)

        max_height = max(left_height, right_height) + 1

        max_dia = max(
            left_height + right_height + 2,
            left_dia,
            right_dia
        )

        return max_height, max_dia

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # how do i know which 3 nodes are included in the Diameter
        # the idea is to cound the edges at each node by adding left and right.

        max_height ,max_dia = self.helper(root)

        return max_dia