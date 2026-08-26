class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=0
        n=0
        if x<0:
            n=1
        x=abs(x)
        while x>0:
            d=x%10
            a = a * 10 + d
            x=x//10
        if a < -2**31 or a > 2**31 - 1:
            return 0
        if n==1 :
            return -a
        else:
            return a
            