class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        count_max = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                count += 1
            else:
                count = 1
            count_max = max(count_max, count)

        return count_max