class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        l=list(s)
        for i in l:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return len(d)