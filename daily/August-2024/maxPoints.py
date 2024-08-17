class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        curr_row = points[0].copy()

        for i in range(rows - 1):
            next_row = [curr_row[0]]

            for j in range(1, cols):
                next_row.append(max(next_row[-1] - 1, curr_row[j]))

            for j in range(cols - 2, -1, -1):
                next_row[j] = max(next_row[j], next_row[j + 1] - 1)

            for j in range(cols):
                curr_row[j] = next_row[j] + points[i + 1][j]

        return max(curr_row)
