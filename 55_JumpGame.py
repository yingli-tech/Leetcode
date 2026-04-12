class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            # This step can’t even be reached, it’s game over right away.
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        # If condition(i > max_reach) is not met, the program can jump to the end of array
        return True