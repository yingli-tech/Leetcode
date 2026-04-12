class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return len(nums)

        length = 1
        prev_diff = 0

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            # These conditions should be separated!
            # diff * prev_diff <=0 does not exclude the case when the list is [0,0].
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                length += 1
                prev_diff = diff
        
        return length