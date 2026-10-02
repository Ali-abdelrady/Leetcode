class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {
            '(' : 1,
            '{' : 2,
            '[' : 3,
            ')' : -1,
            '}' : -2,
            ']' : -3,
        }

        stack = []

        for ch in s:
            if parenthesesMap[ch] > 0:
                stack.append(ch)
                continue

            if len(stack) < 1 or parenthesesMap[ch] + parenthesesMap[stack.pop()] != 0:
                return False

        if len(stack):
            return False

        return True
        