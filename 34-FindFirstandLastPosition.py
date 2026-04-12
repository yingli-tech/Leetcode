class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)

        def match(mid):

            start = mid - 1
            while (start >= 0 and nums[start] == target):
                start -= 1
            
            end = mid + 1
            while (end < length and nums[end] == target):
                end += 1
                
            return [start+1, end-1]

        def binary_search(start, end):

            if start > end:
                return [-1,-1]
            
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return match(mid)
            
            elif nums[mid] > target:
                return binary_search(start, mid-1)
            
            else:
                return binary_search(mid+1, end)

        return binary_search(0, length-1)