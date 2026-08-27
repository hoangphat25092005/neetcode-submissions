class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = len(word1), len(word2)
        merged_ans = []

        for i in range(max(l, r)):
            if i < l:
                merged_ans.append(word1[i])
            if i < r:
                merged_ans.append(word2[i])

        return "".join(merged_ans)