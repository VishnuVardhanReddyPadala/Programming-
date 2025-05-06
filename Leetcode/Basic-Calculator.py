class Solution:
    def calculate(self, s):
        stack = []
        current_num = 0
        sign = 1  # 1 means positive, -1 means negative
        result = 0

        for i, ch in enumerate(s):
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == \+\:
                result += sign * current_num
                current_num = 0
                sign = 1
            elif ch == \-\:
                result += sign * current_num
                current_num = 0
                sign = -1
            elif ch == \(\:
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == \)\:
                result += sign * current_num
                current_num = 0
                result *= stack.pop()
                result += stack.pop()

        if current_num:
            result += sign * current_num
        return result