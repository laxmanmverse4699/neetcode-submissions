class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search would works here. 
        # how Binary search works? => this is to find the the elment in the sorted array.
        # Input: numbers = [1,2,3,4], target = 3
        # Output: [1,2]

        # How about 2 pointers. the array is sorted. 

        i, j = 0, len(numbers)-1

        while(i<j):
            temp_sum = numbers[i] + numbers[j]
            if temp_sum > target:
                j -= 1
            elif temp_sum < target:
                i += 1
            else:
                return [i+1,j+1]
        