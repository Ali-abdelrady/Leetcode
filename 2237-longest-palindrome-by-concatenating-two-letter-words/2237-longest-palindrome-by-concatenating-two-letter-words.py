class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        length = 0 
        has_middle = False

        for word in words:
            rev = word[::-1]
            if count[rev]:
                length += 4
                count[rev] -=1
            else:
                count[word] += 1

        for word in count:
            if word[0] == word[1] and count[word] :
                has_middle = True
                break

        return length + (2 if has_middle else 0)    