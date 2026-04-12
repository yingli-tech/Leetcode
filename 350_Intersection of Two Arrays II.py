class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
 #       dict2 = defaultdict(int)
        out = []

        for i in range(len(nums1)):
            dict1[nums1[i]] = dict1.get(nums1[i], 0) + 1
        for j in range(len(nums2)):
# Because we only need to check existence in dict1, we don't need to build dict2
#            dict2[nums2[j]] = dict2.get(nums2[j], 0) + 1

            if dict1[nums2[j]] != 0:
                out.append(nums2[j])
                dict1[nums2[j]]  -= 1
        
        return out