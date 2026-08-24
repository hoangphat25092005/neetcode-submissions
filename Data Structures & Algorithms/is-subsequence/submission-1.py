class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0:
            return False
        
        if (len(s) == 0 and len(t) == 0) or (len(s) == 0 and len(t) != 0):
            return True

        left, right = 0, 0
        # ans to store the result
        ans = ""

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                ans += s[left]
                left += 1
                right += 1
            else:
                right += 1

        return len(ans) == len(s)