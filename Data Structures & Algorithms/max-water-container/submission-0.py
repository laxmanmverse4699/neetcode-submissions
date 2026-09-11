class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        i, j = 0, len(heights)-1
        while i < j:
            cal_height = (j-i) * min(heights[i], heights[j])
            if max_height < cal_height:
                max_height = cal_height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_height