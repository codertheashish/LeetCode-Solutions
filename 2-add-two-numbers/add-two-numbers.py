# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, head1, head2):
        curr1 = head1
        curr2 = head2

        ans = ListNode(-1)
        curr = ans
        carry = 0

        while curr1 != None or curr2 != None:

            total = carry
            carry = 0

            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next

            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next

            if total >= 10:
                carry = 1
                total -= 10

            newNode = ListNode(total)

            curr.next = newNode
            curr = newNode

        if carry > 0:
            newNode = ListNode(carry)
            curr.next = newNode

        return ans.next