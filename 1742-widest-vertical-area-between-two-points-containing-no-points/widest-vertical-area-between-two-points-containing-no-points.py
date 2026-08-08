class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l=sorted(map(lambda x:x[0],points))
        m=0
        for i in range(len(l)-1):
            m=max(m,l[i+1]-l[i])
        return m