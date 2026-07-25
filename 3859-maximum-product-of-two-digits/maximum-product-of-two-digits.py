class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dig=0
        digs=[]
        while n>0:
            dig=n%10
            digs.append(dig)
            n=n//10
        digs.sort()
        return digs[-2]*digs[-1]

