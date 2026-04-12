class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # Out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            # Water, visited 
            # Note the data format: it's '0' (string), not 0 (integer).
            if grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
            
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        
        return count