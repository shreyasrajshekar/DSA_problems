# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        l=[]
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        v=len(l)-n
        
        if v == 0:
            return head.next
        curr=head
        for _ in range(v- 1):
            curr = curr.next
        curr.next=curr.next.next
        return head