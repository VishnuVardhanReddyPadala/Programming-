class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next