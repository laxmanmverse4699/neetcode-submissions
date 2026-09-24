# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # why do we need to store the items ? it's extra space which we don't need.

        # result = []

        # def travel(root):
        #     if not root:
        #         return
        #     travel(root.left)
        #     result.append(root.val)
        #     if len(result) > k:
        #         return
        #     travel(root.right)
        # travel(root)
        # return result[k-1]
        
        #------------------------------- little optimised

        # efficient way is to notstore the values which we don't need.

        # self.count = 0
        # self.result = None

        # def inorder(root):
        #     if not root:
        #         return 

        #     inorder(root.left)

        #     self.count += 1
        #     if self.count == k:
        #         self.result = root.val
        #         return

        #     inorder(root.right)
        # inorder(root)
        # return self.result

        # ---------------------------- more optimised

        stack = []
        node = root
        
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            k -= 1

            if k == 0 :
                return node.val

            node = node.right
        
