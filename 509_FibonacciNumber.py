class Solution:
    def fib(self, n: int) -> int:
        
        def dfs(n):
            if n == 0 or n == 1:
                return n
            
            f = dfs(n-1) + dfs(n-2)
            return f
        return dfs(n)
