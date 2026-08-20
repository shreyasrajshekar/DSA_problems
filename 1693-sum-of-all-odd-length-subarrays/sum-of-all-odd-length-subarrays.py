class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)

        l=[]
        s=0
        for i in range(n):
            for j in range(i+1,n+1):
                l.append(arr[i:j])
        for i in range(len(l)):
            if len(l[i])%2!=0:
                s+=sum(l[i])
        return s