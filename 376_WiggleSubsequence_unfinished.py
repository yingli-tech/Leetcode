class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        first = 0
        second = 1
        len_sq = 2
        diff_base = 0
        for _ in range(len(nums)-1):
            diff = nums[second] - nums[first]
            if first == 0 or diff == 0:
                diff_base = diff
                second += 1
                first += 1
                continue
            if diff * diff_base < 0:
                len_sq += 1
            else:
                len_sq = 2
            diff_base = diff
            second += 1
            first += 1
        return len_sq        

# Correct version：

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)

        prev = nums[1] - nums[0]
        length = 2 if prev != 0 else 1
        best = length

        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]

            if diff == 0:
                # 完全中断
                length = 1
            elif prev == 0 or diff * prev < 0:
                # 符号相反 → 扩展 wiggle
                length += 1
            else:
                # 符号相同 → 重启连续 wiggle
                length = 2

            prev = diff
            best = max(best, length)

        return best