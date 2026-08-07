class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        l=len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j,k in d.items():
            if k>(l/3):
                r.append(j)
        return r
