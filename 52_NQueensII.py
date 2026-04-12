class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        path = []
        diag1 = set()
        diag2 = set()
        cols = set()

        def backtrack(row):
            if row == n:
                res.append(path[:])
                return
            
            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                path.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)
        # The only difference from 51 N-Queens is we return the count of solutions
        # We don't need to construct the board representation here
        return len(res)