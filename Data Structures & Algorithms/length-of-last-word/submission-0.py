class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove the trailing space in string
        t = s.strip()

        cnt = 0

        for i in range(len(t) - 1, -1, -1):
            if t[i] == ' ':
                return cnt
            cnt += 1

        return cnt