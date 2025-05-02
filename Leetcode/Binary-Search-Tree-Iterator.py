class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def next(self):
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self):
        return bool(self.stack)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
