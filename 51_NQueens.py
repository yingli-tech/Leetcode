class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        cols = set()
        # row - col
        diag1 = set()
        # row + col
        diag2 = set()

        def backtrack(row):
            if row == n:
                # Present the path as a puzzle
                board = []
                for c in path:
                    board.append("."*c + "Q" + "."*(n-c-1))
                res.append(board)
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or row + col in diag2:
                    continue
                
                path.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)
        return res