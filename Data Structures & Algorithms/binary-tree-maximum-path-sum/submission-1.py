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

            left = helper(root.left)
            right = helper(root.right)
            temp = root.val
            if left + temp > temp:
                temp += left
            if right + temp > temp:
                temp += right
            max_result = max(max_result, temp)
            result = root.val
            
            if left > right and result + left > result:
                result += left
            elif result + right > result:
                result += right

            return result
        helper(root)
        return max_result
