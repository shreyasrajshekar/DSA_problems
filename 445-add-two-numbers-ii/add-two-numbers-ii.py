# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = []
        curr = l1

        while curr:
            l.append(curr.val)
            curr = curr.next

        l4 = []
        curr = l2

        while curr:
            l4.append(curr.val)
            curr = curr.next

        i = len(l) - 1
        j = len(l4) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            a = l[i] if i >= 0 else 0
            b = l4[j] if j >= 0 else 0

            total = a + b + carry

            ans.append(total % 10)
            carry = total // 10

            i -= 1
            j -= 1

        ans.reverse()
        dummy = ListNode(0)
        curr = dummy

        for x in ans:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next