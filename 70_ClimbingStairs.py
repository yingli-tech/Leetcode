class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            # Given condition, n is always larger than 1
            return n
        
        # Initiative
        step = [0] * (n+1)
        step[1], step[2] = 1, 2
        
        # 3 is important, otherwise the initials are useless
        for i in range(3, n + 1):
            step[i] = step[i-1] + step[i-2]

        return step[n]