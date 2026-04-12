class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list to facilitate modification.
        s_list = list(s)
        n = len(s)
        
        # Skip 2k characters each time
        for i in range(0, n, 2 * k):
            # Reverse characters within interval [i, i+k) 
            # If left characters are below k, use min(i+k-1, n-1) to ensure no out-of-bounds access
            left = i
            right = min(i + k - 1, n - 1)
            
            # Reverse interval [left, right]
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)