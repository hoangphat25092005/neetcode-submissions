# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # prev is the head of reversed second half
        # Merge two lists
        first = head
        second = prev

        while second:
            tmp1 = first.next # Store the next element of first
            tmp2 = second.next # Store the next element of second

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
