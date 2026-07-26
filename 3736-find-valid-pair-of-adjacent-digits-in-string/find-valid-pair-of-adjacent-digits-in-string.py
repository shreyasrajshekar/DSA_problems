class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1


       
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if d[s[i]] == int(s[i]) and d[s[i + 1]] == int(s[i + 1]):
                    return s[i] + s[i + 1]
        return ""