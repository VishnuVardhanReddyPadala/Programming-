class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        def getHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        height = getHeight(root)
        
        if height == 1:
            return 1
        
        left, right = 0, 2**(height - 1) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exists(root, height, mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return (2**(height - 1) - 1) + left

    def exists(self, root, height, idx):
        left, right = 0, 2**(height - 1) - 1
        for _ in range(height - 1):
            mid = (left + right) // 2
            if idx <= mid:
                root = root.left
                right = mid
            else:
                root = root.right
                left = mid + 1
        return root is not None
