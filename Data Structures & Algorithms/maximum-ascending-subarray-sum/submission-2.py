class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        s = nums[0] 
        for i in range(1, len(nums)):
           if nums[i] > nums[i-1]:
              s = s + nums[i]
              max_sum = max(max_sum, s)
           else:
              s = nums[i]
        return max_sum