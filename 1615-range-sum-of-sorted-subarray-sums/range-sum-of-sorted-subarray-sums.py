class Solution(object):
    def rangeSum(self, nums, n, l, r):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        s=[]
        s1=0
        for left in range(len(nums)):
            curr=0
            for right in range(left, len(nums)):
                curr+=nums[right]
                s.append(curr)
        s.sort()
        print(s)
        for i in range(l-1,r):
            s1+=s[i]
        MOD = 10**9 + 7
        return s1% MOD