class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev=0
        n1=0
        t1=0
        t=0
        s=0
        while n>0:
            t=n%10
            if t!=0:
                rev=rev*10 + t
            n=n//10
        while rev>0:
            t1=rev%10
            n1=n1*10 + t1
            s+=t1
            rev=rev//10
        return s*n1