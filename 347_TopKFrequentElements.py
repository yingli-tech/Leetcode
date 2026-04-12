class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        q = deque()

        for num in nums:
            freq[num] += 1
            # If num already exists in the queue, 
            # remove the forner position at the first
            if num in q:
                q.remove(num)

            # insert the num into an appropriate location based on its frequency of occurrence
            inserted = False
            for i in range(len(q)):
                # The '>=' is to ensure the stable order of the same frequency elements
                # The '=' makes sure that the element that comes first in the original array
                # These two operators have the same effect in this case.
                if freq[num] >= freq[q[i]]:
                    q.insert(i, num)
                    inserted = True
                    break
            if not inserted:
                q.append(num)

        # Take the first k elements from the list
        return list(q)[:k]