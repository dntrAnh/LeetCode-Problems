class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid) 
        regions = 0 
        expanded_grid = [[0] * n * 3 for _ in range(n * 3)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x: int, y: int) -> int:
            if min(x, y) < 0 or max(x, y) >= len(expanded_grid) or expanded_grid[x][y] != 0:
                return 0
            expanded_grid[x][y] = 1
            return 1 + sum(dfs(x + dx, y + dy) for dx, dy in directions)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[i * 3][j * 3 + 2] = expanded_grid[i * 3 + 1][j * 3 + 1] = expanded_grid[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    expanded_grid[i * 3][j * 3] = expanded_grid[i * 3 + 1][j * 3 + 1] = expanded_grid[i * 3 + 2][j * 3 + 2] = 1

        for x in range(n * 3):
            for y in range(n * 3):
                if dfs(x, y) > 0:
                    regions += 1
        
        return regions
