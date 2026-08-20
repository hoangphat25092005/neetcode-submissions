class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        left = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
            
        return left