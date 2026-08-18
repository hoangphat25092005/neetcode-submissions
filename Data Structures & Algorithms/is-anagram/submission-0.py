class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt1 = Counter(s)
        cnt2 = Counter(t)

        print(cnt1, cnt2, sep="\n")

        for i in cnt1:
            if i not in cnt2:
                return False
            elif i in cnt2 and cnt1[i] != cnt2[i]:
                return False

        return True