# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_result = float('-inf')
        
        def helper(root: Optional[TreeNode]) -> int:
            nonlocal max_result
            if not root:
                return 0

            left_gain = max(0, helper(root.left))
            right_gain = max(0, helper(root.right))

            temp = root.val + left_gain + right_gain
            max_result = max(max_result, temp)

            return root.val + max(left_gain, right_gain)

        helper(root)

        return max_result
