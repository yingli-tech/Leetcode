class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        largest = nums[0]
        for x in nums:
            # The sum is nonsense when the sum becomes negative
            if sum < 0:
                sum = 0
            sum += x
            largest = max(largest, sum)
        
        return largest