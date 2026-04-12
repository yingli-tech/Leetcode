class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
                res.append(path[:])
            
            for i in range(start):
                path.append(nums[i])
                backtrack(i + 1, path + [nums[i]])
                path.pop()
                    
        backtrack(0, [])  
        return res