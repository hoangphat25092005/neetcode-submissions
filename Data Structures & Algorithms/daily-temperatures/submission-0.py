class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # [30, 38, 30, 36, 35, 40, 28]
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[i] > st[-1][0]:
                t, idx = st.pop()
                res[idx] = i - idx
            st.append((temperatures[i], i))

        return res