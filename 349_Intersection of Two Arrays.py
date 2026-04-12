class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dict1 = defaultdict(list)
        dict2 = defaultdict(list)
        out = defaultdict(list)

        for i in range(len(nums1)):
            dict1[nums1[i]] = dict1.get(nums1[i], 0) + 1
        for j in range(len(nums2)):
            dict2[nums2[j]] = dict2.get(nums2[j], 0) + 1
            if nums2[j] in dict1:
                out[nums2[j]] = out.get(nums2[j], 0) + 1 
        
        return list(out)
        