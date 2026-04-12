class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])

        # ---- Build Trie ----
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = w   # End flag

        res = set()

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            nxt = node[ch]

            # If find a word
            if "#" in nxt:
                res.add(nxt["#"])

            # Mark visited
            board[r][c] = "#"

            # Explore neighbors
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            board[r][c] = ch

            # Optimization: remove leaf node
            if not nxt:
                node.pop(ch)

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return list(res)