class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = defaultdict(int)
        
        for i in range(len(arr)):
            mp[arr[i]] += 1
            
        cnt = 0
        
        for i in mp:
            if mp[i] == 1:
                cnt += 1
                if cnt == k:
                    return i
        return ""