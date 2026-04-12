class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        index = len(s) - 1
        res = 0

        for i in range(len(g) - 1, -1, -1):
            # Ensure the index is within the list s
            if index < 0:
                break
            
            if g[i] <= s[index]:
                index -= 1
                res += 1
        return res