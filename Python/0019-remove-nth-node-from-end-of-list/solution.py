# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        p1=head
        p2=head
        for i in range(n):
            p2=p2.next
        if p2==None:
            head=head.next
            return head
        while p2.next!=None:
            p2=p2.next
            p1=p1.next
        p1.next=p1.next.next
        return head

        