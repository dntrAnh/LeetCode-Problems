'''
Premium Question 694: https://leetcode.com/problems/number-of-distinct-islands/description/
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
Return the number of distinct islands.

Example 1: 
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2: 
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque() 
        visited = set() 
        islands = set() 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def bfs(row, col) -> List[int]:
            island = []
            queue.append((row, col))
            visited.add((row, col))
            while queue: 
                x, y = queue.popleft() 
                island.append((x - row, y - col))
                for dx, dy in directions: 
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1: 
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return tuple(island)
            
        num_islands = 0
        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == 1 and (row, col) not in visited: 
                    new_island = bfs(row, col)
                    if new_island not in islands: 
                        num_islands += 1 
                        islands.add(new_island)

        return num_islands 
