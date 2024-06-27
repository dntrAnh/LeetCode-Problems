class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for c in range(m): 
            dp[0][c] = 1
        
        for r in range(n): 
            dp[r][0] = 1
        
        for r in range(1, n): 
            for c in range(1, m): 
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[-1][-1]
