class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        d = {}

        for word in s1.split():
            d[word] = d.get(word, 0) + 1

        for word in s2.split():
            d[word] = d.get(word, 0) + 1

        ans = []

        for word in d:
            if d[word] == 1:
                ans.append(word)

        return ans