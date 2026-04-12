class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        phone = {
            "2" : "abc", "3" : "def", "4" : "ghi",
            "5" : "jkl", "6" : "mno", "7" : "pqrs",
            "8" : "tuv", "9" : "wxyz"
        }

        def backtrack(index):
            # Both index and len(path) are appropriate here.
            if len(path) == len(digits):
                res.append("".join(path))
                # Return is very important
                return

            letters = phone[digits[index]]
            for ch in letters:
                path.append(ch)
                backtrack(index + 1)
                path.pop()
            
        backtrack(0)
        return res
            