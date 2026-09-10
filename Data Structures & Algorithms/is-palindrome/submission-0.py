class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(s.lower())
        filter_s = [c for c in s_list if c.isalnum()]
        s2 = "".join(filter_s[::-1])
        if "".join(filter_s) == s2:
            return True
        else:
            return False