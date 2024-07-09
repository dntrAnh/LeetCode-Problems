class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_dict = {}

        for row in grid:
            row_str = ','.join(map(str, row))
            if row_str not in row_dict:
                row_dict[row_str] = 1
            else:
                row_dict[row_str] += 1
        
        result = 0

        for col_idx in range(n):
            col_str = ','.join(str(grid[row_idx][col_idx]) for row_idx in range(n))
            if col_str in row_dict:
                result += row_dict[col_str]
        
        return result
