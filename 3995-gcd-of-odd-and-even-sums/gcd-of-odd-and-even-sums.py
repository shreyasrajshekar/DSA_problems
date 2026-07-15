import fractions
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return fractions.gcd(n * n, n * (n + 1))