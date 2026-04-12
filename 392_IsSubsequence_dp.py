class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s) 
        n2 = len(t) 
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        max1 = 0

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n1][n2] == n1