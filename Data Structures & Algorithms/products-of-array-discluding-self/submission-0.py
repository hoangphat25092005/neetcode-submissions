class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zeros = 0
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt_zeros += 1
            else:
                prod *= nums[i]
        
        if cnt_zeros > 1:
            return [0] * len(nums)

        output = []

        for i in range(len(nums)):
            if cnt_zeros:
                if nums[i] == 0:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                nums[i] = prod // nums[i]
                output.append(nums[i])

        return output
