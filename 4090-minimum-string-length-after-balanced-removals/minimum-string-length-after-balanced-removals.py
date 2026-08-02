class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        l=list(s)
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]]=1
            else:
                d[l[i]]+=1
        val_a = d.get("a", 0)
        val_b = d.get("b", 0)
        return abs(val_a - val_b)