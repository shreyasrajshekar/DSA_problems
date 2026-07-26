class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high=len(nums)-1
        low=0
        sear=0
        while low<=high:
            sear=low+(high-low)//2
            if nums[sear]==target:
                return sear
            elif nums[sear]>target:
                high=sear-1
          
            else:
                low=sear+1
        return -1