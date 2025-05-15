class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        i = 0 
        res = [words[i]]

        for j in range(1,len(words)):
            if groups[j] != groups[i]:
                res.append(words[j])
                i = j

        return res