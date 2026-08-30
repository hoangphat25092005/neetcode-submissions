class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mp = defaultdict(int)

        ans = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                mp[grid[i][j]] += 1

        for i in range(1, len(grid) ** 2 + 1):
            if mp[i] >= 2:
                ans.append(i)
            elif mp[i] < 1:
                ans.append(i)

        ans = sorted(ans, key=mp.get, reverse=True)    
        return ans