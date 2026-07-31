class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = mn = ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                mx, mn = mn, mx

            mx = max(nums[i], mx * nums[i])
            mn = min(nums[i], mn * nums[i])

            ans = max(ans, mx)

        return ans