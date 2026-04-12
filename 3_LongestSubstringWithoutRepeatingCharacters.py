class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = {}
        left = 0
        start = 0
        max_length = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:
                start = left
                current_length = right - left
                if max_length < current_length:
                    max_length = current_length
                while s[left] != c:
                    window[s[left]] -= 1
                    left += 1
                if s[left] == c:
                    window[c] -= 1
                    left += 1
        return max_length