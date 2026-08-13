class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i % 2 == 0:
                d[i] = d.get(i, 0) + 1
                 
        ans = -1
        max_freq = 0
        for k,v in d.items():
            if v > max_freq or (v == max_freq and k < ans):
                max_freq = v
                ans = k
        return ans
        