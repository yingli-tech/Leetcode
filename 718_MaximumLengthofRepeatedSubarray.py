class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # The length is always greater than 0， so I initialize max1 to 0， not -inf
        max1 = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max1 = max(max1, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return max1