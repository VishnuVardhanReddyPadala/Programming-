class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next
            reversed_head = reverseLinkedList(prev_group.next, next_group)

            temp = prev_group.next
            prev_group.next = reversed_head
            temp.next = next_group
            prev_group = temp
