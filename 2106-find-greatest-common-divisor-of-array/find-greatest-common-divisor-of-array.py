import fractions
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        l=min(nums)
        return fractions.gcd(m,l)