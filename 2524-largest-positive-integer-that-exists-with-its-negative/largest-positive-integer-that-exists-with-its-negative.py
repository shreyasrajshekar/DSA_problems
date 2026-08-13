class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif abs(nums[i]) in nums:
                t=max(t,abs(nums[i]))
        if t==0:
            return -1
        else:
            return t