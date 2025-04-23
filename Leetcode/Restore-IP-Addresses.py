class Solution:
    def restoreIpAddresses(self, s):
        res = []
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(\.\.join(path))
                return
            for i in range(1, 4):
                if start + i <= len(s):
                    part = s[start:start + i]
                    if (part[0] == '0' and len(part) > 1) or not (0 <= int(part) <= 255):
                        continue
                    backtrack(start + i, path + [part])
        backtrack(0, [])
        return res