class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt_h = [0] * 101
        
        for h in heights:
            cnt_h[h] += 1
        
        expected = []
        for i in range(1, 101):
            c = cnt_h[i]
            for _ in range(c):
                expected.append(i)
        
        ans = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1

        return ans