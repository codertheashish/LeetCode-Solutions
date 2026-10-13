
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find cycle length
        length = 1
        current = slow.next

        while current != slow:
            current = current.next
            length += 1

        # Step 3: Find cycle starting node
        slow = head
        fast = head

        for i in range(length):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
