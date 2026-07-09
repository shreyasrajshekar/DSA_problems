class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        low=0
        high=len(s)-1
        h=len(s)
        if h%2==0:
            mid=(low+high)//2
        else:
            mid=(low+high)//2+0.5
        while low<=high:
            if s[low]==s[high]:
                return low
            else:
                low=low+1
                high=high-1
        return -1
        
