class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0 or (x, y) in visited:
                return
            visited.add((x, y))
            island.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        island = []
        
        found = False
        for row in range(rows):
            if found:
                break
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break

        queue = deque()
        for x, y in island: 
            queue.append((x, y, 0))
        
        while queue:
            x, y, distance = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if grid[nx][ny] == 1:
                        return distance
                    queue.append((nx, ny, distance + 1))
                    visited.add((nx, ny))
        
        return -1
