class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            # this row is to ignore the characters out of the mapping
            else:
                continue
        return len(stack) == 0 
    
a = Solution()
b = a.isValid("(sadasf){}")
print(b)
