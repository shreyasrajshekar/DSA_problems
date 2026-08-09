class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a = list(d.values())
        a.sort()
        for i in range(1,len(a)):
            if a[i-1]==a[i]:
                return False
        return True