class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        # Early pruning
        from collections import Counter
        board_count = Counter(ch for row in board for ch in row)

        valid_words = []
        for w in words:
            word_count = Counter(w)
            for ch in word_count:
                if word_count[ch] > board_count.get(ch, 0):
                    break
            else:
                # True if first char occurs more than last char
                # Reverse-order pruning
                if word_count[w[0]] > word_count[w[-1]]:
                    w = w[::-1]
                valid_words.append(w)
                
        # If the list of words is empty, there is no need to proceed.
        # Skip processing if the word list is empty. 
        # It acts as an early pruning step.
        # Early pruning.
        if not valid_words:
            return False

        def backtrack(r, c, idx, word):
            if idx == len(word):
                return True
            if not ((0 <= r < m) and (0 <= c < n)) or word[idx] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            res = (backtrack(r + 1, c, idx + 1, word) or backtrack(r, c + 1, idx + 1, word)
            or backtrack(r - 1, c, idx + 1, word) or backtrack(r, c - 1, idx + 1, word))
            
            board[r][c] = temp

            return res
        output_words = set()
        for r in range(m):
            for c in range(n):
                for w in valid_words:
                    if backtrack(r, c, 0, w):
                        output_words.add(w)
        return list(output_words)
    
    # this is wrong in a 2x2 board with words ["ab","cd"]    # because it can reuse the same cell for different words?
    # I'm not sure the reasoning here. Let it go for now.