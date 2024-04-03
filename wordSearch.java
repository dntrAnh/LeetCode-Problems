class Solution 
{
    char[][] matrix; 
    char[] letters;
    boolean[][] visited;
    public boolean exist(char[][] board, String word) 
    {
        int rowLength = board.length;
        int colLength = board[0].length;
        matrix = board; 
        letters = word.toCharArray();
        for (int r = 0; r < rowLength; r++) {
            for (int c = 0; c < colLength; c++) {
                if (board[r][c] == letters[0]) {
                    visited = new boolean[rowLength][colLength];
                    boolean result = dfs(r, c, 0);
                    if (result == true) {
                        return true;
                    }
                }
            }
        }
        return false; 
    }

    private boolean dfs(int currRow, int currCol, int currIdx)
    {
        // base case
        if (currIdx == letters.length) {
            return true;
        }
        if ((currRow < 0 || currRow >= matrix.length)
        || (currCol < 0 || currCol >= matrix[0].length)) {
            return false; 
        }
        if (visited[currRow][currCol] == true) {
            return false;
        }
        if (matrix[currRow][currCol] != letters[currIdx]) {
            return false; 
        }
        visited[currRow][currCol] = true; 

        // dfs all 4 directions 
        boolean top = dfs(currRow - 1, currCol, currIdx + 1);
        boolean down = dfs(currRow + 1, currCol, currIdx + 1);
        boolean left = dfs(currRow, currCol - 1, currIdx + 1);
        boolean right = dfs(currRow, currCol + 1, currIdx + 1);

        boolean ans = top || down || left || right; 
        if (ans == false) {
            visited[currRow][currCol] = false;
        }
        return ans;
    }
}
