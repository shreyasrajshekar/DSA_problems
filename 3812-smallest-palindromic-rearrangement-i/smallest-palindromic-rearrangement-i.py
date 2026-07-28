class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        d = {}
        mid = ""

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for k, i in sorted(d.items()):
            if i % 2 == 1:
                mid = k
            for j in range(i // 2):
                l.append(k)

        first = "".join(l)
        return first + mid + first[::-1]