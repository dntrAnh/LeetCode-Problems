class Solution 
{
    public int shortestPathAllKeys(String[] grid) 
    {
        int y = grid.length, x = grid[0].length(), maskKeys = 0;
        int visited[][][] = new int[y][x][64];

        LinkedList<int[]> q = new LinkedList<>();
        for (int i = 0; i != y; ++i) {
            for (int j = 0; j != x; ++j) {
                char ch = grid[i].charAt(j);
                if (ch == '@') {
                    q.add(new int[] { 0, i, j }); 
                }    
                else if (ch > 'Z') {
                    maskKeys |= 1 << (ch - 'a');
                }
            }
        }

        for (int lev = 0; !q.isEmpty(); ++lev) {
            for (int n = q.size(); n != 0; --n) {
                int t[] = q.pollFirst(); 
                int key = t[0], r = t[1], c = t[2];

                if (r == -1 || r == y || c == -1 || c == x || visited[r][c][key] == 1)
                    continue;

                char ch = grid[r].charAt(c);
                if (ch == '#') {
                    continue;
                }

                if (ch > '@' && ch < 'a') {
                    if ((key & (1 << (ch - 'A'))) == 0) {
                        continue;
                    }
                        
                }

                if (ch > 'Z') { 
                    key |= 1 << (ch - 'a');
                    if (key == maskKeys) {
                        return lev;
                    }
                }

                visited[r][c][key] = 1;

                q.addLast(new int[] { key, r - 1, c });
                q.addLast(new int[] { key, r + 1, c });
                q.addLast(new int[] { key, r, c - 1 });
                q.addLast(new int[] { key, r, c + 1 });
            }
        }
        return -1;
    }
}
