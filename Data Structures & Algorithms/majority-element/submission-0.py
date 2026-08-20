class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # handle edge case
        if len(nums) == 1:
            return nums[0]
        
        cnt = Counter(nums)

        length = len(nums) // 2

        for i in cnt:
            if cnt[i] > length:
                
                return i

        raise ValueError("No such value")