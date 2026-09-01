class Solution:
    def check(self, nums: List[int]) -> bool:
        # nums = [3, 4, 5, 1, 2] => [1, 2, 3, 4, 5]
        # nums = [2, 1, 3, 4] => [1, 2, 3, 4]
        cnt = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                cnt += 1
                if cnt > 1: return False
        
        return True