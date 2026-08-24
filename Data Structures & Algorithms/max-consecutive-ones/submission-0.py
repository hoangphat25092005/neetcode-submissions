class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        
        j = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                j += 1
                max_cons = max(max_cons, j)
            else:
                j = 0
        
        return max_cons