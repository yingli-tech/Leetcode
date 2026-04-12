class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(heights), len(heights[0])
        
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        
        directions =[(1,0), (-1,0), (0,1), (0,-1)] 

        def dfs(i, j, visited):
            visited[i][j] = True

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if (
                    # Go out of boundaries
                    x < 0 or x >= m or y < 0 or y >= n
                    # This cell already can flow to an ocean 
                    # And it's unnecessary to search again 
                    or visited[x][y]
                    # Reverse flow cannot go from high to low.
                    or heights[x][y] < heights[i][j]
                ):
                    continue
                dfs(x, y, visited)


        # Left boundary
        for i in range(m):
            dfs(i, 0, pac)
        # Top boundary
        for j in range(n):
            dfs(0, j, pac)


        # Right boundary
        for i in range(m):
            dfs(i, n - 1, atl)
        # Bottom boundary
        for j in range(n):
            dfs(m - 1, j, atl)        

        for i in range(m):
            for j in range(n):
                if atl[i][j] and pac[i][j]:
                    res.append([i, j])

        return res