class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque() 
        visited = set() 

        fresh = 0 
        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == 2: 
                    rotten.append((row, col))
                    visited.add((row, col))
                elif grid[row][col] == 1: 
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        minutes = 0
        while rotten  and fresh > 0: 
            minutes += 1
            for _ in range(len(rotten)): 
                x, y = rotten.popleft() 
                for dx, dy in directions: 
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1: 
                        fresh -= 1
                        visited.add((nx, ny)) 
                        rotten.append((nx, ny)) 
        
        if fresh == 0: 
            return minutes 
        else: 
            return -1 
