#https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1 
        right = len(arr)-2
        while left <= right:
            mid = (left + right)//2
            if arr[mid] > arr[mid-1] and arr[mid+1] < arr[mid]:
                return mid
            if arr[mid+1] < arr[mid-1]:
                right = mid - 1
            else:
                left = mid + 1
