class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=len)
        res = []
        print(sorted_words)
        for i in range(len(sorted_words)-1):
            for j in range(i+1,len(sorted_words)):
                if sorted_words[i] in sorted_words[j]:
                    print("found")
                    res.append(sorted_words[i])
                    break
        return res