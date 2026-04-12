class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        index_i = 0
        index_j = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    # dp[i][j] indicates whether the substring s[i..j] (inclusive) is a palindrome.
                    dp[i][j] = True
                    if j - i >= index_j - index_i:
                        index_i = i
                        index_j = j
        
        return s[index_i:index_j+1]
