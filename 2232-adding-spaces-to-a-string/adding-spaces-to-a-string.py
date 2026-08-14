class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        a = []
        spaces = set(spaces)

        for i in range(len(s)):
            if i in spaces:
                a.append(" ")
            a.append(s[i])

        return "".join(a)