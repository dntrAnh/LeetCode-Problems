class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        row_mins = [min(row) for row in matrix]
        col_maxs = [max(matrix[i][j] for i in range(rows)) for j in range(cols)]

        lucky_numbers = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                    lucky_numbers.append(matrix[i][j])

        return lucky_numbers
