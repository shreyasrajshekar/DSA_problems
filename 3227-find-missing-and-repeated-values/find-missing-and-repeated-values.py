class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        d={}
        for i in grid:
            for j in i:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
        l=[]
        for k , v in d.items():
            if v>1:
                l.append(k)
        for k in range(1, len(grid) * len(grid) + 1): 
            if k not in d: 
                l.append(k)
        return l
            