class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting : O(n.log(n))
        # set : O(n)
        # sliding window : O(n)

        # time : O(n log(n))
        
        
        sorted_list = list(set(nums))
        sorted_list = sorted(sorted_list)
        if len(sorted_list) < 2:
            return len(sorted_list)
        left = 0
        right = 1
        result = 1
        while right < len(sorted_list):
            if sorted_list[right]-1 != sorted_list[right-1]:
                left = right
            
            result = max(result, right-left+1)
            right += 1
        return result