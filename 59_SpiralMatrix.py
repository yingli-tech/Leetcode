class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1

        while left < right and top < bottom:
            # top: from left to right
            for j in range(left, right):
                matrix[top][j] = num
                num += 1

            # right: from top to bottom
            for i in range (top, bottom):
                matrix[i][right] = num
                num += 1
            
            # bottom: from right to left
            for j in range (right, left, -1):
                matrix[bottom][j] = num
                num += 1
            
            # left: from bottom to top
            for i in range(bottom, top, -1):
                matrix[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if n%2 == 1:
            matrix[n//2][n//2] = num
        
        return matrix