class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        so = sorted(d.items(), key=lambda x: x[1], reverse=True)

        a = []
        for k, v in so:
            a.append(k * v)

        return "".join(a)