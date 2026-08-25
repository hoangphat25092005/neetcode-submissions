class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize the dictionary to store the key
        mp1 = defaultdict(str)
        mp2 = defaultdict(str)

        for a, b in zip(s, t):
            if a in mp1 and mp1[a] != b:
                return False
            if b in mp2 and mp2[b] != a:
                return False

            mp1[a] = b
            mp2[b] = a

        return True 