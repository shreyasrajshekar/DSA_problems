class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        d = {}
        left = 0

        for right in range(len(nums)):
            i = nums[right]

            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

            while d[i] > k:
                d[nums[left]] -= 1
                left += 1

            s = max(s, right - left + 1)

        return s