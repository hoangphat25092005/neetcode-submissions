class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        increase, decrease = 1, 1 # variable track
        maxx = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase += 1
                decrease = 1
            elif nums[i] < nums[i - 1]:
                decrease += 1
                increase = 1
            else:
                decrease = 1
                increase = 1
            
            maxx = max(maxx, increase, decrease)

        return maxx