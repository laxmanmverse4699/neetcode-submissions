# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if l1.next == None:
        #     temp = l1.val + l2.val
        #     l1.val = temp % 10
        #     rem = temp // 10
        #     if rem > 0:
        #         temp_node = ListNode()
        #         temp_node.val = rem
        #         l1.next = temp_node
        #     return l1
        
        # prev = None
        # current = l1

        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node
        # l1 = prev

        # prev = None
        # current = l2

        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node
        # l2 = prev

        head = l1
        l1_prev = l1
        reminder = 0
        while l2 and l1:
            temp_sum = l1.val + l2.val + reminder
            l1.val = temp_sum % 10
            reminder = temp_sum // 10

            l1_prev = l1
            l2 = l2.next
            l1 = l1.next

        while l1:
            temp_sum = l1.val + reminder
            l1.val = temp_sum % 10
            reminder = temp_sum // 10

            l1_prev = l1
            l1 = l1.next


        while l2:
            temp_sum = l2.val + reminder
            
            temp_node = ListNode()
            temp_node.val = temp_sum % 10
            reminder = temp_sum // 10
            l1_prev.next = temp_node
            l1_prev = l1_prev.next
            l2 = l2.next
        
        if reminder > 0:
            temp_node = ListNode()
            temp_node.val = reminder
            l1_prev.next = temp_node
            l1_prev = l1_prev.next

        return head

        # prev = None
        # current = head

        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node
        # return prev
        

