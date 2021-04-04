class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"{": "}", "[": "]", "(": ")"}
        for char in s:
            if char in d:
                stack.append(d[char])
            if char in d.values():
                if stack == [] or char != stack.pop():
                    return False
        return stack == []