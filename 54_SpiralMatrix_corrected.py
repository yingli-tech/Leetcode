class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m is the number of the row and n is the number of the col
        m = len(matrix) 
        n = len(matrix[0])
        left, top, right, bottom = 0, 0, n - 1, m - 1
        target = []

        while left <= right and top <= bottom:
            # Please notice the left boundry!
            # From left to right
            for col in range(left, right + 1):
                target.append(matrix[top][col])
            top += 1

            # From top to bottom
            for row in range(top, bottom + 1):
                target.append(matrix[row][right])
            right -= 1

            # From right to left and the condition is to avoid the row vector
            if top <= bottom:
                for col in range(right, left - 1, - 1):
                    target.append(matrix[bottom][col])
                bottom -= 1

            # From bottom to top and the condition is to avoid the column vector
            if left <= right:
                for row in range(bottom,top - 1, - 1):
                    target.append(matrix[row][left])
                left += 1

        return target


