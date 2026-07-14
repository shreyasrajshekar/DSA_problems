class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sorted(nums)
        m=0
        left=0
        right=len(s)-1
        while(left<right):
            m=max(s[left]+s[right],m)
            left+=1
            right-=1
        return m