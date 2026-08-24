class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        
        n=num<0
        num=abs(num)

        r=[]
        while num>0:
            r.append(str(num%7))
            num//=7

        if n:
            r.append("-")
        return "".join(r[::-1])