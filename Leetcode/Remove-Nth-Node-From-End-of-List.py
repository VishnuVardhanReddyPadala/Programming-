# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        first = second = dummy

        # Move 'first' n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until 'first' reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node
        second.next = second.next.next

        return dummy.next  # Return the updated head
