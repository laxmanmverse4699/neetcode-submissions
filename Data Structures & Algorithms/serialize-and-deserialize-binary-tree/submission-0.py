# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        result = []
        dq = deque([root])
        result.append(root.val)
        while dq:
            for i in range(len(dq)):
                current = dq.popleft()

                if current.left:
                    dq.append(current.left)
                    result.append(current.left.val)
                else:
                    result.append(None)
                if current.right:
                    dq.append(current.right)
                    result.append(current.right.val)
                else:
                    result.append(None)

        while result and result[-1] is None:
            result.pop()
        text = ",".join("None" if x is None else str(x) for x in result)
        return text

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        values = [
            None if part.strip() == "None" else int(part.strip())
            for part in data.split(",")
            if part.strip()
        ]
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values):
                if values[i] is not None:
                    node.left = TreeNode(values[i])
                    queue.append(node.left)
                i += 1

            if i < len(values):
                if values[i] is not None:
                    node.right = TreeNode(values[i])
                    queue.append(node.right)
                i += 1

        return root
