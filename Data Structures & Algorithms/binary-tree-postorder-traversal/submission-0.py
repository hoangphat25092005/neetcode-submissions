# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.right is None or (ans and ans[-1] == root.right.val):
                ans.append(root.val)
                root = None
            else:
                stack.append(root)
                root = root.right

        return ans