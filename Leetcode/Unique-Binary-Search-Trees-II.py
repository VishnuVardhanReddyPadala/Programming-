class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.build(1, n)
    
    def build(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start, end + 1):
            left = self.build(start, i - 1)
            right = self.build(i + 1, end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
