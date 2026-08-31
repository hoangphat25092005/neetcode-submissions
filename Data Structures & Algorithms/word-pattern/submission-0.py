class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # turn s to the str list for easy mapping
        s = s.split(" ")

        if len(pattern) != len(s): return False

        mp1 = {}
        mp2 = {}

        for i, j in zip(pattern, s):
            if i in mp1 and mp1[i] != j:
                return False
            if j in mp2 and mp2[j] != i:
                return False

            mp1[i] = j
            mp2[j] = i

        return True