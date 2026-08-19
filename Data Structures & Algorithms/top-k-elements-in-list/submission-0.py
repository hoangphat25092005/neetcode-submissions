class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for i in range(len(nums)):
            frequent[nums[i]] = frequent.get(nums[i], 0) + 1


        frequent = sorted(frequent, key=frequent.get, reverse=True)

        return frequent[:k]