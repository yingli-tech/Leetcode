class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, target):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # This is the key to speed up the process.
                if candidates[i] > target:
                    break
                # 'i > start' is not only to ensure the i - 1 > 0, 
                # But also to give a chance to get the only one combination which meets the target. 
                # A same number cannot be used twice in one layer.                                 
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                path.pop()

        backtrack(0, target)

        return res