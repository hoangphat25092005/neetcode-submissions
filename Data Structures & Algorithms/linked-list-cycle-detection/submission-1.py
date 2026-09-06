# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If empty list node occured
        if head is None: return False

        # We can you fast and slow pointer for this problem
        slow = fast = head

        while fast and fast.next:
            if slow == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next

        return False