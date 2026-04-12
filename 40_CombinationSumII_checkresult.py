class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        # Sort the original list
        # To ensure consistent ordering of the combinations (whose sums meet the target)
        # It allows duplicates to be efficiently eliminated.
        candidates.sort()

        def backtrack(start, target):
            if target < 0:
                return
            if target == 0: 
                if path not in res:
                    res.append(path[:])
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                path.pop()

        backtrack(0, target)

        return res