class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Avoid redundant checks and the condition i<j
                if nums[i] + nums[j] == target:
                    return [i, j]
                

# the class solution is needed in leetcode instead of using the function
# there is no need to give the input code, and the result should be a return value

# another solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], idx]
            hashmap[num] = idx
        return []  # 题目保证有解，此行仅为语法完整性