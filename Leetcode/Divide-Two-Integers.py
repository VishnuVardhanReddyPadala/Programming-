class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Perform the division using bit manipulation
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
