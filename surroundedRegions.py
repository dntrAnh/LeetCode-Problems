class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque()
        
        for i in range(rows):
            for j in (0, cols - 1):
                if board[i][j] == 'O':
                    queue.append((i, j))
                    
        for j in range(cols):
            for i in (0, rows - 1):
                if board[i][j] == 'O':
                    queue.append((i, j))
        
        def in_bounds(x, y):
            return 0 <= x < rows and 0 <= y < cols
                
        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'O':
                board[x][y] = '#'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if in_bounds(nx, ny) and board[nx][ny] == 'O':
                        queue.append((nx, ny))
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
