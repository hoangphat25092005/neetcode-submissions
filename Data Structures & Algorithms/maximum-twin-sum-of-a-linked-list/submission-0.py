# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        # We can reverse the second half of a linkedlist
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverseLinkedList(slow)
        l, r = head, slow
        maxx = 0
        while r:
            maxx = max(maxx, r.val + l.val)
            r = r.next
            l = l.next

        return maxx