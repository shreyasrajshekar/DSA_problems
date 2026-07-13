class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=s.split()
        for i in range(len(l1)):
            l1[i] = l1[i][::-1]
        f=" ".join(l1)
        return f