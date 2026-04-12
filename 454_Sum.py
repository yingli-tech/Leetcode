class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum1 = defaultdict(int)
        count = 0
        # Store the sum of two arrays
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                temp = nums1[i] + nums2[j]
                sum1[temp] += 1
        
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                comple = 0 - (nums3[k] + nums4[l])
                # Add the corresponding frequencies
                if comple in sum1:
                    count += sum1[comple]

        return count