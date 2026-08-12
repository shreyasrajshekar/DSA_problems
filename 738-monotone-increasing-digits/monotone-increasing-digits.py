class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = list(map(int, str(n)))

        for i in range(len(l) - 1, 0, -1):
            if l[i - 1] > l[i]:
                l[i - 1] -= 1
                for j in range(i, len(l)):
                    l[j] = 9

        return int(''.join(map(str, l)))




                