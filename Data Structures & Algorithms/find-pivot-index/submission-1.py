class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_nums = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            prefix_nums[i + 1] = prefix_nums[i] + nums[i] 
        
        for i in range(len(nums)):
            left = prefix_nums[i]
            right = prefix_nums[len(nums)] - prefix_nums[i + 1]
            if left == right:
                return i

        return -1