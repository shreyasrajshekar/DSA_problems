class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        l=0
        
        for nums in s:
            if nums-1 not in s:
                l1=1
                while nums+l1 in s:
                    l1+=1
                l=max(l,l1)
        return l