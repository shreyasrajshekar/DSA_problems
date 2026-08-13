class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        t=''.join(word1)
        t1="".join(word2)
        if t==t1:
            return True
        return False