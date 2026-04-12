class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        stack = []
        while right < len(nums) + 1:
            maxi = float('-inf')
            for i in range(left, right, 1):
                temp = nums[i]
                if temp > maxi:
                    maxi = temp
            stack.append(maxi)
            right += 1
            left += 1
        return stack