class Solution:
    def minSubArrayLen(self, s, nums):
        result = sys.maxsize  # The final result is initialized to the maximum integer.
        sum_val = 0  # the sum of the sliding window
        i = 0  # initialized position of the sliding window
        sub_length = 0  # the length of the sliding window
        for j in range(len(nums)):
            sum_val += nums[j]
            # update i(starting point) and compare the sum and the result
            while sum_val >= s: # this while is very important to try to shrink the left boundary of the sliding window. 
                sub_length = j - i + 1  # the length of the sub array
                result = min(result, sub_length)
                sum_val -= nums[i]  # important, this is how the sliding window works
                i += 1
        return 0 if result == sys.maxsize else result