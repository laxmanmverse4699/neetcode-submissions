class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if len(strs) > 0:
            for item in strs:
                result += str(len(item)) + "#" + item
        return result
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            result.append(s[j:j+length])
            i = j + length
        return result