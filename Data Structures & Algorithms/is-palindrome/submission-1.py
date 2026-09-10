class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = list(s.lower())
        str_filtered = [item for item in str_list if item.isalnum()]
        s2 = "".join(str_filtered[::-1])
        if "".join(str_filtered) == s2:
            return True
        else:
            return False