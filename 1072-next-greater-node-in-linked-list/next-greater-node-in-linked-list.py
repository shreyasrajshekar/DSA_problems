# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        r = []
        stack = []
        v = []
        curr = head
        i = 0
        while curr:
            v.append(curr.val)
            r.append(0)
            while stack and v[stack[-1]] < curr.val:
                idx = stack.pop()
                r[idx] = curr.val
            stack.append(i)
            curr = curr.next
            i += 1
        return r