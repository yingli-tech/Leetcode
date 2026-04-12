class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                window[s[left]] -= 1
                left += 1
	#update the length of windows every time	
            max_length = max(max_length, right - left + 1)

        return max_length