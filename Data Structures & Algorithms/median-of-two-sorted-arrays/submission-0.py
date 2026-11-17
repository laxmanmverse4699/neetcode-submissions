class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        for element in nums2:
            left, right = 0, len(nums1)-1
            
            while left <= right:
                mid = (left+right) // 2
                
                if nums1[mid] == element:
                    left = mid
                    break
                elif nums1[mid] < element:
                    left = mid+1
                else:
                    right = mid-1
            nums1.insert(left, element)

        median = len(nums1) // 2
        if len(nums1) % 2 > 0:
            return nums1[median]
        else:
            return (nums1[median-1] + nums1[median])/ 2
        
        