class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count the occurrence frequency of each character in t
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        
        # record the occurence frequency of each character in the current window
        window = defaultdict(int)
        left = 0  # left boundrt of the slide
        valid = 0  # record the number of characters that meet the requirement in the current window
        start = 0  # starting index of the minimum substring 
        min_length = float('inf')  # the length of the minimum substring
        
        for right in range(len(s)):
            # move the right pointer to expand the window
            c = s[right]
            if c in target:
                window[c] += 1
                # increment valid by 1 when the count of a character in the window meets the target requirement
                if window[c] == target[c]:
                    valid += 1
            
            # when the window includes all characters in t, try to shrink the left boundry
            while valid == len(target):
                # update the minimum substring
                current_length = right - left + 1
                if current_length < min_length:
                    start = left
                    min_length = current_length
                
                # move left pointer to shrink the window
                left_c = s[left]
                if left_c in target:
                    # if a character that meets the requirement is removed, decrease valid by 1
                    if window[left_c] == target[left_c]:
                        valid -= 1
                    window[left_c] -= 1
                left += 1
        
        # Return if a valid substring is found; otherwise, return an empty string.
        return "" if min_length == float('inf') else s[start:start+min_length]