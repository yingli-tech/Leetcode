class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(startIndex: int):
            # Recursive termination condition: when the combination length reaches k
            if len(path) == k:
                # Save the current combination
                result.append(path[:])  
                return

            # Horizontal traversal: choose from startIndex onwards
            for i in range(startIndex, n + 1):
                # Process the node
                path.append(i)     
                # Recursively traverse vertically, next layer starts from i+1         
                backtracking(i + 1)         
                # Backtrack, undo the processed node
                path.pop()

        backtracking(1)
        return result
         