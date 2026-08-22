class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=n
        s=0
        d=0
        m=1
        while n>0:
            d=n%10
            s+=d
            m*=d
            n=n//10
        if t%(s+m)==0:
            return True
        return False