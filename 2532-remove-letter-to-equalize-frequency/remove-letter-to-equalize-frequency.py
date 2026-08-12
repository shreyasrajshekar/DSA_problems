class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l = list(word)
        d = {}

        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        v = list(d.values())

        for i in range(len(v)):
            x = v[:]
            x[i] -= 1

            if x[i] == 0:
                x.pop(i)

            if len(set(x)) == 1:
                return True

        return False