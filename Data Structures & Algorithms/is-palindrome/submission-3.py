class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        s = s.lower()
        s = s.strip()
        #s = s.replace(" ", "")
        for i in range(len(s)):
            if s[i].isalnum():
                tmp += s[i]
        
        return tmp == tmp[::-1]