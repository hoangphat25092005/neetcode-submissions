class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # nums = [1, 7, 3, 6, 5, 6] => index = 3 with value 6
        tmp = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = tmp - left_sum - nums[i]
            if right_sum == left_sum:
                return i

            left_sum += nums[i]

        return -1