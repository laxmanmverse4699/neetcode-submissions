# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast!= None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        # slow is middle now
        
        prev = None
        current = slow.next

        slow.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # reveresed and joined with original
        # now reorder

        first = head
        second = prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
                



