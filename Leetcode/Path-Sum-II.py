# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        def helper(node, remaining_sum, path, result):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == remaining_sum:
                result.append(list(path))
            else:
                helper(node.left, remaining_sum - node.val, path, result)
                helper(node.right, remaining_sum - node.val, path, result)
            path.pop()

        result = []
        helper(root, sum, [], result)
        return result
        