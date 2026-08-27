class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        l=list(s)
        for i in range(len(s)):
            if l[i] not in d:
                d[l[i]]=1
            else:
                return l[i]
        return -1