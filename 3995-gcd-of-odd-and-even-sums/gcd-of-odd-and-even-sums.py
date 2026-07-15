import fractions
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        so, se = 0, 0
        o, e = 1, 2

        for i in range(n):
            so += o
            se += e
            o += 2
            e += 2

        return fractions.gcd(so, se)