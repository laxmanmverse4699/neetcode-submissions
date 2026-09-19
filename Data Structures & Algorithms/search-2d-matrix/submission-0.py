class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0, len(matrix)-1

        while i <= j:
            mid = (i+j)//2

            if matrix[mid][0] > target:
                j = mid - 1
            elif matrix[mid][-1] < target:
                i = mid + 1
            else:
                left, right = 0, len(matrix[mid])-1
                while left <= right:
                    mid2 = (left+right)//2

                    if matrix[mid][mid2] > target:
                        right = mid2 - 1
                    elif matrix[mid][mid2] < target:
                        left = mid2 + 1
                    else:
                        return True
                return False
        return False