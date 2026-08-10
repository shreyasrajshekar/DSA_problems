class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        f = 0

        for i in sentences:
            l = i.split()
            m = len(l)
            f = max(f, m)

        return f