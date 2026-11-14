class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_filtered = [item for item in list(s.lower()) if item.isalnum()]
        return str_filtered == str_filtered[::-1]