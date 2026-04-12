class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet = []
        n = len(nums)

        for i in range(n-2):
            # Avoid the duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplet.append([nums[i], nums[left], nums[right]])
                    # Skip the same value for the second number
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip the same value for the third number                
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplet




            