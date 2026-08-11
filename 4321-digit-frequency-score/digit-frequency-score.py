class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        dig=0
        while n>0:
            dig=n%10
            if dig not in d:
                d[dig]=1
            else:
                d[dig]+=1
            n=n//10
        res=0
        temp=0
        for k,v in d.items():
            temp=k*v
            res+=temp
            temp=0
        return res