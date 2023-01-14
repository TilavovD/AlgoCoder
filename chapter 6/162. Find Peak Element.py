class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        left = 1 
        right = len(nums)-2
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[mid-1] and nums[mid+1] < nums[mid]:
                return mid
            if nums[mid+1] < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return 0 if nums[0]> nums[1] else len(nums) -1
