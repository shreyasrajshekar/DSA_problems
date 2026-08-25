# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        s=True
        while s:
            s=False
            curr=head
            while curr and curr.next:
                
                if curr.val>curr.next.val:
                    curr.val,curr.next.val=curr.next.val,curr.val
                    s=True
                curr=curr.next
        return head