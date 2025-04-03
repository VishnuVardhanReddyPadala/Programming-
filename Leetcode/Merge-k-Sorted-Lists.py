from heapq import heappush, heappop

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        dummy = ListNode()
        current = dummy

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
