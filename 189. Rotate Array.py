# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)//2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]
        for i in range((k%len(nums))//2):
            nums[i], nums[k%len(nums)-i-1] = nums[k%len(nums)-i-1], nums[i]
        for i in range((len(nums) - (k%len(nums)))//2):
            nums[i+k%len(nums)], nums[-i-1] = nums[-i-1], nums[i+k%len(nums)]
