class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ''.join(sorted(list(s))) == (''.join(sorted(list(t)))):
            return True
        return False