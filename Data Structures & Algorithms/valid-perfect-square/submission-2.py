
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        ans = math.isqrt(num)
        return ans * ans == num