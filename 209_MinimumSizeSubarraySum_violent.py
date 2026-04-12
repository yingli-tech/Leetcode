class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = sys.maxsize
        length = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum >= target:
                    length = j - i + 1
                    result = min(result,length)
                    break
        return 0 if result == sys.maxsize else result
                