class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        for i in range(len(nums)):
            d=0
            s=0
            while nums[i]>0:
                d=nums[i]%10
                s+=d
                nums[i]=nums[i]//10
            if s==i:
                return i\
           
        return -1
