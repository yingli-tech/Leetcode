class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        def dfs(i, j):

            # Out of bounds, water, and visited
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                # Return 0, not None.
                return 0
            
            grid[i][j] = 0

            area = 1 + dfs(i, j - 1) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i + 1, j)

            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
                    
        
        return max_area