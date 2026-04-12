class Solution:
    def reverse(self, s: list, start: int, end: int) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    def removespace(self, s: list):
        i = 0        
        slow = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        while i < n:
            if s[i] != ' ':
                s[slow] = s[i]
                slow += 1
            elif s[i] == ' ' and i + 1 < n and s[i+1] != ' ':
                s[slow] = ' '
                slow += 1
            i += 1
            
        if slow > 0 and s[slow-1] == ' ':
            slow -= 1

        del s[slow:]

    def reverseWords(self, s: str) -> str:
        begin = 0
        # Transform the str to list
        s1 = list(s)

        self.removespace(s1)
        n = len(s1)        
        self.reverse(s1, begin, n-1)

        for i in range(len(s1) + 1):
            # The order of below two conditions is very important.
            # Because when i equals the length of the list s1, 
            # accessing s1[i] will trigger an index out of range error 
            # (since the maximum valid index of a list is len(s1) - 1).
            if i == len(s1) or s1[i] == ' ':
                self.reverse(s1, begin, i - 1)
                begin = i + 1

        return ''.join(s1)
