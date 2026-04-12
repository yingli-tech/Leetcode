class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # double pointers
        slow = 0
        n = len(nums) # calcute the length before the loop to decrease repeated computing.
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
        