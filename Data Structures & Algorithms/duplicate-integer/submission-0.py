class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        mp = {}

        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 0
            else:
                mp[nums[i]] += 1
                if mp[nums[i]] >= 1:
                    return True

        return False