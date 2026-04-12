class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Store the indexs in the queue
        # Using this index is to slide the window
        q = deque()
        res = []
        for i in range(len(nums)):
            # Remove all indexs at the end of the queue that are smaller than the current element.
            # The '=' is to ensure no duplicate of the number exist.
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # Slide current window
            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res