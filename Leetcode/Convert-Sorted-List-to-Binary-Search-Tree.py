# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None

        def find_middle(left, right):
            slow, fast = left, left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def build_tree(left, right):
            if left == right:
                return None

            mid = find_middle(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)

            return root

        return build_tree(head, None)