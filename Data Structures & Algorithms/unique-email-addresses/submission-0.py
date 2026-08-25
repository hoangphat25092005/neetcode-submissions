class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ans = set()

        for e in emails:
            # split local and domain name
            tmp1, tmp2 = e.split("@")
            tmp1 = tmp1.split("+")[0]
            tmp1 = tmp1.replace(".", "")
            ans.add((tmp1, tmp2))
        
        return len(ans)