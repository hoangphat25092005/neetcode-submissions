class Solution:
    def maxDifference(self, s: str) -> int:
        mp = defaultdict(int)

        for ch in s:
            mp[ch] += 1

        max_odd = 0
        min_even = float("inf")

        for ch, freq in mp.items():
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even