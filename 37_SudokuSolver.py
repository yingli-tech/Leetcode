class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # Initial the contraints
        # row
        for r in range(9):
            # column
            for c in range(9):
                if board[r][c] != ".":
                    x = board[r][c]
                    rows[r].add(x)
                    cols[c].add(x)
                    index = (r // 3) * 3 + (c//3)
                    boxes[index].add(x)
        
        def backtrack(r, c):
            if c == 9:
                return backtrack(r + 1, 0)
            if r == 9:
                return True
            
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for x in "123456789":
                index = (r // 3) * 3 + (c // 3)
                # Please remeber these constraints
                # They are the part of the key information
                # Especially how to calculate the index
                if x in rows[r] or x in cols[c] or x in boxes[index]:
                    continue
                
                board[r][c] = x
                rows[r].add(x)
                cols[c].add(x)
                
                boxes[index].add(x)
                
                if backtrack(r, c + 1):
                    return True
                # This recover step is very important!
                # Remeber put "." back
                board[r][c] = "."
                rows[r].remove(x)
                cols[c].remove(x)
                boxes[index].remove(x)
            
            return False
        
        backtrack(0,0)