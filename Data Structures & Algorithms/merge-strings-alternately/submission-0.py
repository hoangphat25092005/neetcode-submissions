class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        merged_ans = []

        while l < len(word1) and r < len(word2):
            merged_ans.append(word1[l])
            merged_ans.append(word2[r])
            l += 1
            r += 1

        if len(word1) > len(word2):
            for i in range(l, len(word1)):
                merged_ans.append(word1[i])
        else:
            for j in range(r, len(word2)):
                merged_ans.append(word2[j])

        return ''.join(merged_ans)