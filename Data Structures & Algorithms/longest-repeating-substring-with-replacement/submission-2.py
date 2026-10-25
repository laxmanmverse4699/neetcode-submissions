class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # char -> how many times it's in the window
        left = 0
        max_freq = 0        # highest count of any char in the window
        best = 0

        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1

            # Only the char just added can raise the max
            max_freq = max(max_freq, count[ch])

            # Too many replacements needed, so shrink from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best