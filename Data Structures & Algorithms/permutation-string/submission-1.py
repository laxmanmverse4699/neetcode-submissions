class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        start = 0
        end = len(s1)-1
        permStr = False
        while end < len(s2):
            temp = list(s1)
            i = start
            isPerm = True
            while i <= end:
                if s2[i] in temp:
                    temp.remove(s2[i])
                else:
                    isPerm = False
                    break
                i += 1
            if isPerm:
                permStr = True
                break
            start += 1
            end += 1
        return permStr