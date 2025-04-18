class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current and current.next:
            first = current
            second = current.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            current = first.next

        return dummy.next
