class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m is the number of the row and n is the number of the col
        m = len(matrix) 
        n = len(matrix[0])
        left, top, right, bottom = 0, 0, n - 1, m - 1
        target = [0] * (m * n)  
        num = 0

        while left <= right and top <= bottom:
            
            for col in range(right + 1):
                target.append(matrix[top][col])
                target[num] = matrix[top][col]
                num += 1
            top += 1

            for row in range(top, bottom + 1):
                target[num] = matrix[row][right]
                num += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, - 1):
                    target[num] = matrix[bottom][col]
                    num += 1
                bottom -= 1

            if left <= bottom:
                for row in range(bottom,top - 1, - 1):
                    target[num] = matrix[row][left]
                    num += 1
                left += 1

        return target


