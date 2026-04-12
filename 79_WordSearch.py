class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        # Early pruning: if the word has more characters than the board, immediately return false
        from collections import Counter
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        for ch in word_count:
            if word_count[ch] > board_count.get(ch, 0):
                return False
        # True if first char occurs more than last char
        # Reverse-order pruning
        if word_count[word[0]] > word_count[word[-1]]:
            word = word[::-1]

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if not ((0 <= r < m) and (0 <= c < n)) or word[idx] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            res = (backtrack(r + 1, c, idx + 1) or backtrack(r, c + 1, idx + 1)
            or backtrack(r - 1, c, idx + 1) or backtrack(r, c - 1, idx + 1))
            
            board[r][c] = temp

            return res

        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        return False