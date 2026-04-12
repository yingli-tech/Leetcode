class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        def binary_search(start: int, end:int):
            if start > end:
                return -1
            mid = (start + end) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start, mid-1)
            else:
                return binary_search(mid+1, end)

        return binary_search(0, length-1)  
        # either recursively or iteratively