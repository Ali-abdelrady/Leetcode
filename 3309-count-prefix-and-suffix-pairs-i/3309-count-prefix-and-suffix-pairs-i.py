class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n1 , n2 = len(str1) , len(str2)
            if n1 > n2:
                return False
            
            if str1 in str2[:n1] and str1 in str2[n2-n1:]:
                return True
        res = 0 
        n = len(words)
        for i in range(n-1):
            for j in range(i+1 , n):
                if isPrefixAndSuffix(words[i],words[j]):
                    res += 1

        return res