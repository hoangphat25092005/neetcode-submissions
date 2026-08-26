class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = [] # define a stack
        mp = defaultdict(lambda: -1) # if missing key auto return -1

        for i in range(len(nums2)):
            while st and nums2[i] > st[-1]:
                mp[st[-1]] = nums2[i]
                st.pop()
            st.append(nums2[i])

        return [mp[i] for i in nums1]