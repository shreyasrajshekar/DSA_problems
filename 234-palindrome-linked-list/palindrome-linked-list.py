# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr=head
        l=[]
        while curr:
            l.append(curr.val)
            curr=curr.next
        if l == l[::-1]:
            return True
        return False