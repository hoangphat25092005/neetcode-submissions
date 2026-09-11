class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            k_sum = (mid * (mid + 1)) // 2
            if k_sum > n:
                right = mid - 1
            else:
                left = mid + 1
                ans = max(ans, mid)

        return ans