class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False]*len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                # If you remove the return, the logic is still correct.
                # Loop runs until the end of range, but nothing is appended
                # But it will be performing an extra O(n) loop check
                # Affects performance (especially when length is large)
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
        
        backtrack()
        return res

