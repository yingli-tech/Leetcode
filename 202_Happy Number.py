class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        seen = set()

        while n != 1:
            if n in seen:
                return False
            # Sum is a local variable, and its value in former cycle vanishes at this point.    
            seen.add(n)
            # An easy way to calculate the sum of squares of digits
            n = sum(int(d)**2 for d in str(n))
#            digits = [int(d) for d in str(n)]
#            sum = 0
#            for i in range(len(digits)):
#                sum += digits[i]*digits[i]    

#            n = sum

        return True