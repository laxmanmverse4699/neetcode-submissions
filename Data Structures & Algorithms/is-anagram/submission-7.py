class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # sorted method
        return sorted(s) == sorted(t)

        # counter method
        #return Counter(s) == Counter(t)
        