class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        av = []

        i=0
        j=len(nums)-1

        while i<j:
            a=(nums[i]+nums[j])/2.0
            av.append(a)

            i+=1
            j-=1

        return min(av)
