class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        l=[0]
        for i in gain:
            l.append(i+l[-1])
        if max(l)>0:
            return max(l)
        else:
            return 0