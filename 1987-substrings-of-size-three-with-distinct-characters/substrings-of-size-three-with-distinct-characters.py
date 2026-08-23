class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        c = [s[i:i+3] for i in range(len(s) - 2)]
        co=len(c)
        for i in range(len(c)):
            d={}
            for j in c[i]:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
            if max(d.values())!=1:
                co-=1
        return co