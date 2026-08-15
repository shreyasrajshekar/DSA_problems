class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}

        # Count characters
        for i in s:
            d[i] = d.get(i, 0) + 1

        # Check if possible
        for i in d:
            if d[i] > (len(s) + 1) // 2:
                return ""

        ans = ""
        prev = ""

        while len(ans) < len(s):
            maxchar = ""
            maxcount = 0

            for i in d:
                if d[i] > maxcount and i != prev:
                    maxchar = i
                    maxcount = d[i]

            if maxchar == "":
                return ""

            ans += maxchar
            d[maxchar] -= 1
            prev = maxchar

        return ans
        