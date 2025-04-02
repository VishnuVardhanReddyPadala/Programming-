class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  
        
        original, reversed_x = x, 0

        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return original == reversed_x