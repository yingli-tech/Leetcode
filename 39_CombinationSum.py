class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, target):
            # Two conditions to stop
            # 1. target == 0 means we found a valid combination
            if target == 0:
                res.append(path[:])  # Found a valid combination
                return
            # Because candidates are all positive integers and there are not limit on the number of times each candidate can be used.
            if target < 0:
                return

            # Start from 'start' to avoid duplicates
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])  # The same number can be used multiple times
                path.pop()  # Backtrack
        backtrack(0, [], target)
        return res