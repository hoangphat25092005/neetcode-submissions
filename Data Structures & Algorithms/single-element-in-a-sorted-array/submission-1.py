class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if ((mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])):
                return nums[mid]
                
            size_left = mid - 1 if nums[mid - 1] == nums[mid] else mid
            if size_left % 2 == 0:
                l = mid + 1
            else:
                r = mid - 1

        return -1