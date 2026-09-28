# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        curr=head
        while curr!=None and curr.next!=None:
            if curr.next.val==curr.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head

        