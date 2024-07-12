"""
286. Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])

        queue = deque()
        for row in range(rows): 
            for col in range(cols): 
                if rooms[row][col] == 0: 
                    queue.append((row, col))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue: 
            x, y = queue.popleft() 
            for dx, dy in directions: 
                nx, ny = dx + x, dy + y 
                if 0 <= nx < rows and 0 <= ny < cols and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))
