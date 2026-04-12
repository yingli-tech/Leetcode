class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            # use sorted s as the key
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []

            # add s to the corresponding group
            groups[key].append(s)

        # return all groups
        return list(groups.values())