class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def startsAndEndsWithVowel(str):
            if str[0] in vowels and str[-1] in vowels :
                return 1
            return 0
        vowels = {
            'a' : True,
            'e' : True,
            'i' : True,
            'o' : True,
            'u' : True}
        prefix = []
        prefix.append(startsAndEndsWithVowel(words[0]))

        for i in range(1,len(words)):
            prefix.append(prefix[i-1] + startsAndEndsWithVowel(words[i]))

        res = []
        for (start,end) in queries :
            if start == 0 :
                res.append(prefix[end])
            else:
                res.append(prefix[end] - prefix[start - 1])

        return res

       