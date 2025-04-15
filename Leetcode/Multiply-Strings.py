class Solution:
    def multiply(self, num1, num2):
        if num1 == \0\ or num2 == \0\:
            return \0\

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1

                sum_ = mul + result[pos2]
                result[pos2] = sum_ % 10
                result[pos1] += sum_ // 10

        res_str = ''.join(map(str, result)).lstrip('0')
        return res_str or '0'
