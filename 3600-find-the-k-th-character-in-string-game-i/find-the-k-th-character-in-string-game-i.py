class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        s = "a"

        while len(s) < k:
            s += ''.join(chr(ord(c) + 1) for c in s)

        return s[k - 1]
