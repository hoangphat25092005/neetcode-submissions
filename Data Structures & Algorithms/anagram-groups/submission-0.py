class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        
        mp = defaultdict(list)

        for i in strs:
            tmp = ''.join(sorted(i))
            mp[tmp].append(i)
        
        return list(mp.values())
        