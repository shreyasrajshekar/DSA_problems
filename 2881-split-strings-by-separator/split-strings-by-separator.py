class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        l = []
        for word in words:
            a = word.split(separator)
            for j in a:
                if j != "":
                    l.append(j)

        return l
                