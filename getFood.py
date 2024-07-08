class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    queue.append((i, j))
                    visited.add((i, j))
                    break
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        steps = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        if grid[nx][ny] == "O":
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                        elif grid[nx][ny] == "#":
                            return steps + 1
            steps += 1

        return -1
