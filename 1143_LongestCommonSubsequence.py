class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1) 
        n2 = len(text2) 
        # dp[i][j] represents the length of the Longest Common Subsequence (LCS)
        # between the first i characters(前i个) of text1 and the first j characters of text2
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        max1 = 0

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n1][n2]