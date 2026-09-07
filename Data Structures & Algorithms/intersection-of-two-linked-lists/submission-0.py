# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def countNode(self, head: ListNode) -> int:
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None: return headB
        if headB is None: return headA
        if headA and headB is None: return None

        lengA = self.countNode(headA)
        lengB = self.countNode(headB)

        l1 = headA
        l2 = headB

        if lengA < lengB:
            lengA, lengB = lengB, lengA
            l1, l2 = l2, l1

        while lengA - lengB:
            lengA -= 1
            l1 = l1.next

        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l1