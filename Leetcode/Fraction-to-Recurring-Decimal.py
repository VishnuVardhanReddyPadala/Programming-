class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return \0\

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        numerator, denominator = abs(numerator), abs(denominator)
        quotient, remainder = divmod(numerator, denominator)
        result.append(str(quotient))

        if remainder == 0:
            return ''.join(result)

        result.append('.')
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, '(')
                result.append(')')
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            result.append(str(digit))

        return ''.join(result)
