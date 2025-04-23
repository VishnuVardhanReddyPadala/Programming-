class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def dfs(i, j, length):
            key = (i, j, length)
            if key in memo:
                return memo[key]

            if s1[i:i+length] == s2[j:j+length]:
                memo[key] = True
                return True

            if sorted(s1[i:i+length]) != sorted(s2[j:j+length]):
                memo[key] = False
                return False

            for k in range(1, length):
                if (dfs(i, j, k) and dfs(i + k, j + k, length - k)) or \\
                   (dfs(i, j + length - k, k) and dfs(i + k, j, length - k)):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(0, 0, len(s1))
