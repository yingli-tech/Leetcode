class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, length):
            if len(path) == length:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, length)
                path.pop()
                    
        for length in range(len(nums) + 1):
            backtrack(0, length)  
        return res