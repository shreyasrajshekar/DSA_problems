class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        a = sorted(set(arr))
        rank = {}

        for i, num in enumerate(a):
            rank[num] = i + 1

        return [rank[x] for x in arr]