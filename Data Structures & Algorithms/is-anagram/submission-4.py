class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if ''.join(sorted(list(s))) == (''.join(sorted(list(t)))):
        #     return True
        # return False

        s_s = collections.Counter(s)
        s_t = collections.Counter(t)
        if len(s) < len(t):
            s_s, s_t = s_t, s_s
        result = s_s - s_t
        for val in result.values():
            if val > 0:
                return False
        return True