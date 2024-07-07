class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dpX = [[0] * cols for _ in range(rows)]
        dpY = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'X':
                    dpX[i][j] = 1
                elif grid[i][j] == 'Y':
                    dpY[i][j] = 1
                
                if i > 0:
                    dpX[i][j] += dpX[i-1][j]
                    dpY[i][j] += dpY[i-1][j]
                if j > 0:
                    dpX[i][j] += dpX[i][j-1]
                    dpY[i][j] += dpY[i][j-1]
                if i > 0 and j > 0:
                    dpX[i][j] -= dpX[i-1][j-1]
                    dpY[i][j] -= dpY[i-1][j-1]

        def count_in_submatrix(x1, y1, x2, y2, dp):
            total = dp[x2][y2]
            if x1 > 0:
                total -= dp[x1-1][y2]
            if y1 > 0:
                total -= dp[x2][y1-1]
            if x1 > 0 and y1 > 0:
                total += dp[x1-1][y1-1]
            return total

        valid_count = 0
        for x2 in range(rows):
            for y2 in range(cols):
                count_x = count_in_submatrix(0, 0, x2, y2, dpX)
                count_y = count_in_submatrix(0, 0, x2, y2, dpY)
                if count_x == count_y and count_x > 0:
                    valid_count += 1
                    
        return valid_count
