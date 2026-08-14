class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in range(len(nums)):
            if nums[i]!=0:
                l.append(nums[i])
            elif nums[i]==0:
                count+=1
        for i in range(count):
            l.append(0)
        return l


