class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        sd=0
        snd=0
        for i in range (1,n+1):
            if i%m==0:
                sd+=i
            else:
                snd+=i
        return snd-sd