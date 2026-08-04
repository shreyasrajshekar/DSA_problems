class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        mi=min(nums)
        mx=max(nums)
        while mi<mx:
            if mi not in nums:
                l.append(mi)
                mi+=1
            else:
                mi+=1
        return l