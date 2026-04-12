from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}  # a directionary to record the number of each fruit within the window
        left = 0  # the left boundary of the window
        max_length = 0  # maxium length of the window
        
        for right in range(len(fruits)):
            # add current fruit to the window
            current_fruit = fruits[right]
            fruit_count[current_fruit] = fruit_count.get(current_fruit, 0) + 1
            
            # shrink the left boundary when the types of fruit within the window exceed 2
            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                # delete the fruit from the dictionary when its number deceases to 0
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                left += 1  # move left pointer to right
            
            # update the maxium length of the window
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length