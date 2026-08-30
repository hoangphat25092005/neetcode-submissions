class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tmp = "balloon"

        mp1 = defaultdict(int)
        mp2 = defaultdict(int)

        for i in range(len(tmp)):
            mp1[tmp[i]] += 1

        ans = float("inf")

        for i in range(len(text)):
            if text[i] in mp1:
                mp2[text[i]] += 1

        for i in range(len(tmp)):
            if mp2[tmp[i]] == 0:
                return 0

            ans = min(ans, mp2[tmp[i]] // mp1[tmp[i]])
        
        return ans
        