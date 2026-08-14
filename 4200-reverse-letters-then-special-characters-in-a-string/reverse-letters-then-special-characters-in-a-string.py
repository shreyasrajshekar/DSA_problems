class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        t = []
        r = []

        for i in range(len(l)):
            if l[i].isalpha():
                t.append(l[i])
            elif not l[i].isalnum():
                r.append(l[i])

        t = t[::-1]
        r = r[::-1]

        j = 0
        k = 0

        for i in range(len(l)):
            if l[i].isalpha():
                l[i] = t[j]
                j += 1
            elif not l[i].isalnum():
                l[i] = r[k]
                k += 1

        return ''.join(l)