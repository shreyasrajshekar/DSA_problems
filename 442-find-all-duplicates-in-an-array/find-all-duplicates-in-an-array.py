class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        a=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k, v in d.items():
            if v==2:
                a.append(k)
        return a