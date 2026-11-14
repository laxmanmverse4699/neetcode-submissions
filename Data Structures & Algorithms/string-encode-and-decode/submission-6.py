class Solution:

    def encode(self, strs: List[str]) -> str:
        collector = []
        for item in strs:
            collector.append(f"{len(item)}#{item}")
        return "".join(collector)
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