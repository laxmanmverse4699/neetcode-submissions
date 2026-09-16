class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {"[" : "]", "{": "}", "(": ")"}
        data = list(s)
        for char in range(len(data)):
            if data[char] == '(' or data[char] == '{' or data[char] == '[':
                stack.append(data[char])
            else:
                if len(stack) < 1:
                    return False
                temp_char = stack.pop()
                match_char = store.get(temp_char)
                if match_char == data[char]:
                    continue
                else:
                    return False
        print(stack)
        if len(stack) > 0:
            return False
        return True
        