class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return helper(left + 1, right) or helper(left, right - 1)

            left += 1
            right -= 1

        return True