class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])
        p=0

        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    for dr,dc in directions:
                        nr=r+dr
                        nc=c+dc
                        if (nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]==0):
                            p+=1
        return p