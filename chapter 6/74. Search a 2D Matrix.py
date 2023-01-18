# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid][0]>target:
                right = mid - 1
            elif matrix[mid][-1]<target:
                left = mid + 1
            else:
                break
        if left>right:
            return False
        left = 0
        right = len(matrix[mid])-1
        while left<=right:
            mid2 = (left+right)//2
            if matrix[mid][mid2]>target:
                right = mid2 - 1
            elif matrix[mid][mid2]<target:
                left = mid2 + 1
            else:
                return True
        return False
