class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best_len = 0
        
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            best_len = max(best_len, right - left + 1)
        
        return best_len
            

