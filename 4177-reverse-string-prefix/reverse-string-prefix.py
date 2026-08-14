class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r=[]
        t=[]
        l=list(s)
        for i in range(len(l)):
            if i <k:
                r.append(l[i])
            else:
                t.append(l[i])
        return ''.join(r[::-1]+t)