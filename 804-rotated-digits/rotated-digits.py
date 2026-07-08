class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        for num in range(1, n + 1):
            good = False
            valid = True

            for ch in str(num):
                if ch in "347":
                    valid = False
                    break
                if ch in "2569":
                    good = True

            if valid and good:
                count += 1

        return count