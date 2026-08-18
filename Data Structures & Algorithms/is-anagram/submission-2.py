class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = {}

        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = 1
            else:
                mp[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in mp:
                return False
            else:
                mp[t[j]] -= 1

        for i in mp:
            if mp[i] != 0:
                return False
            
        return True
    