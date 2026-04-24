class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for start, end in intervals:
            if start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]
            elif end < newInterval[0]:
                res.append([start, end])
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        
        res.append(newInterval)

        return res
