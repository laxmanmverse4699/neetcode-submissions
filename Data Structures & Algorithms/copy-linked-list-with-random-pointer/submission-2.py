"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        current = head

        while current:
            copy = Node(current.val)
            copy.next = current.next
            copy.random = current.random

            current.next = copy
            current = copy.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        start = head.next
        orig = head
        copy = start

        while orig:
            orig.next = copy.next
            orig = orig.next
            if orig:
                copy.next = orig.next
                copy = copy.next

        return start
        