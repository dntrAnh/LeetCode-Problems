class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(x: int, y: int):
            queue = deque([(x, y)])
            visited[x][y] = True

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

        for row in range(rows):
            for col in range(cols):
                # at the edge 
                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and grid[row][col] == 1 and not visited[row][col]:
                    bfs(row, col)

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    count += 1

        return count
