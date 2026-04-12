class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicate elements
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Pruning: if the current number is greater than the target, break directly
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                path.pop()

        backtrack(0, target)
        return res