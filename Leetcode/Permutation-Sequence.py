class Solution(object):
    def getPermutation(self, n, k):
        \\\
        :type n: int
        :type k: int
        :rtype: str
        \\\
        import math
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = []

        for i in range(n):
            fact = math.factorial(n - 1 - i)
            index = k // fact
            result.append(nums.pop(index))
            k %= fact

        return ''.join(result)
