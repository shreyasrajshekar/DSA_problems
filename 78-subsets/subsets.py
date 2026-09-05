class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[[]]
        for i in nums:
            l+=[j + [i] for j in l]
        return l