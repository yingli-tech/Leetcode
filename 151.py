class Solution:
    def reverse(self, s: list, start: int, end: int) -> None:
        """Reverse the string in place from start to end (inclusive)."""
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def remove_extra_spaces(self, s: list) -> None:
        """Remove leading, trailing, and multiple spaces between words."""
        n = len(s)
        i = 0
        slow = 0

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        while i < n:
            # Copy non-space characters
            if s[i] != ' ':
                s[slow] = s[i]
                slow += 1
            # Handle single space between words
            elif s[i] == ' ' and i + 1 < n and s[i + 1] != ' ':
                s[slow] = ' '
                slow += 1
            i += 1

        # Remove trailing space if present
        if slow > 0 and s[slow - 1] == ' ':
            slow -= 1
        # Delete the elements from the index slow (including the index slow)
        del s[slow:]

    def reverseWords(self, s: str) -> str:
        """Reverse the order of words in a string."""
        s_list = list(s)
        self.remove_extra_spaces(s_list)  # Clean up spaces
        self.reverse(s_list, 0, len(s_list) - 1)  # Reverse entire string

        start = 0
        for i in range(len(s_list) + 1):
            if i == len(s_list) or s_list[i] == ' ':
                self.reverse(s_list, start, i - 1)  # Reverse each word
                start = i + 1

        return ''.join(s_list)