# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        if not root:
            return None

        if root.left:
            self.flatten(root.left)
            temp = root.right
            root.right = root.left
            root.left = None

            while root.right:
                root = root.right
            root.right = temp

        if root.right:
            self.flatten(root.right)
            