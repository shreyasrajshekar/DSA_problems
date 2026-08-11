class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i, dig in enumerate(nums):
            if dig not in d:
                d[dig]=i
            else:
                if abs(i-d[dig])<=k:
                    return True
                else:
                    d[dig]=i
        return False