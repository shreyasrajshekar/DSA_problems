class Solution(object):
    def countKthRoots(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        if k == 1:
            return r - l + 1

        ans = 0
        x = 0

        while True:
            y = 1
            for _ in range(k):
                y *= x
                if y > r:
                    break

            if y > r:
                break

            if l <= y <= r:
                ans += 1

            x += 1

        return ans