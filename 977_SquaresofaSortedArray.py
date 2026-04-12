class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        while i <= j:
            square_i = nums[i] * nums[i]
            square_j = nums[j] * nums[j]
            if square_i > square_j:
                result[k] = square_i
                i += 1
            else:
                result[k] = square_j
                j -= 1
            k -= 1
        return result