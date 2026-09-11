class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
            
        # Find the index of the highest pillar in the array
        max_idx = 0
        for i in range(len(height)):
            if height[i] > height[max_idx]:
                max_idx = i
        
        water_stored = 0
        
        # 1. Left-to-Right Pass (Stops at the highest peak)
        piller1, piller2 = 0, 1
        temp_sum = 0
        while piller2 <= max_idx:  # Scan up to the maximum peak
            if height[piller1] == 0:
                piller1 = piller2
                piller2 += 1
                continue
            
            if height[piller2] >= height[piller1]:
                water_stored += (((piller2) - piller1 - 1) * height[piller1]) - temp_sum
                piller1 = piller2
                temp_sum = 0
            else:
                temp_sum += height[piller2]
            piller2 += 1
            
        # 2. Right-to-Left Pass (Scans from the end back to the highest peak)
        piller1, piller2 = len(height) - 1, len(height) - 2
        temp_sum = 0
        while piller2 >= max_idx:
            if height[piller1] == 0:
                piller1 = piller2
                piller2 -= 1
                continue
                
            if height[piller2] >= height[piller1]:
                water_stored += ((piller1 - piller2 - 1) * height[piller1]) - temp_sum
                piller1 = piller2
                temp_sum = 0
            else:
                temp_sum += height[piller2]
            piller2 -= 1
            
        return water_stored
