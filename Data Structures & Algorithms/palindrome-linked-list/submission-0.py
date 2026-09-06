# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedlist(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
    
        # Find the middle
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        # Reverse the second half
        right = self.reverseLinkedlist(slow)
    
        # Compare first half and reversed second half
        left = head
    
        while right:
            if left.val != right.val:
                return False
    
            left = left.next
            right = right.next
    
        return True
        