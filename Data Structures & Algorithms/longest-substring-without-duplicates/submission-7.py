class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     last_seen = {}
    #     left = 0
    #     best_len = 0
        
    #     for right, char in enumerate(s):
    #         if char in last_seen and last_seen[char] >= left:
    #             left = last_seen[char] + 1
    #         last_seen[char] = right
    #         best_len = max(best_len, right - left + 1)
        
    #     return best_len
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        best_len = 0

        for right in range(len(s)):
            # 1. expand: try to include s[right] in window state
            while s[right] in window:
                # 2. shrink from left until valid again
                window.remove(s[left])
                left += 1
            window.add(s[right])

            # 3. update answer using current valid window [left, right]
            best_len = max(best_len, right - left + 1)

        return best_len

