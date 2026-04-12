class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        cur_max = 0
        count = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == cur_max:
                count += 1
                cur_max = max_reach
        
        return count