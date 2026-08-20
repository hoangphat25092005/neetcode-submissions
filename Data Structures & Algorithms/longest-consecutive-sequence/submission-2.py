class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        st = set(nums)
        max_length = 0

        for num in st:
            if num - 1 not in st:
                res, cur = 0, num
                while cur in st:
                    res += 1
                    cur += 1
                max_length = max(max_length, res)
        
        return max_length
