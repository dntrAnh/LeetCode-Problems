class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i: int, j: int):
            queue = deque([(i, j)])
            visited.add((i, j))

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        def count_islands() -> int:
            nonlocal count
            count = 0
            visited.clear()
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        count += 1
                        bfs(i, j)
            return count
        
        if count_islands() != 1:
            return 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2
