class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.insert(0, level)
            queue = next_queue

        return result